# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import datetime

from interviewTest.decorators import is_approved, is_signup_complete
from interviewTest.forms import ClientAccountForm, OtherInfoForm
from interviewTest.models import ClientAccount


def home(request):
    return render(request, 'interviewtest/home.html')


def convert_date(date_obj):
    return datetime.datetime.strptime(date_obj, "%m/%d/%Y").strftime("%Y-%m-%d")

def generate_client_id():
    return randint(10000000, 999999999)

def save_client_account(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        try:
            user.clientaccount
        except:
            email = response.get('email')
            first_name = response.get('first_name')
            last_name = response.get('last_name')
            gender = str(response.get('gender')).title()
            try:
                dob =response.get('birthday')
                dob = convert_date(dob)
            except:
                dob = None
            client_id = generate_client_id()
            newclient = ClientAccount.objects.create(user=user,gender=gender,DOB=dob,client_id=client_id)
            newclient.save()

    if backend.name == 'github':
        try:
            user.clientaccount
        except:
            email = response.get('email')
            client_id = generate_client_id()
            newclient = ClientAccount.objects.create(user=user, client_id=client_id)
            newclient.save()

@login_required
def complete_sign_up(request):
    if not request.user.clientaccount.signup_complete:
        if request.method == 'POST':
            form = ClientAccountForm(request.POST,use_required_attribute=False)
            if form.is_valid():
                form.save()
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                if (user and user.is_active):
                    login(request, user)
                    return redirect(reverse('profile'))
        else:
            data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'username': request.user.username,
                'gender': request.user.clientaccount.gender,
                'dob': request.user.clientaccount.DOB,
            }
            form = ClientAccountForm(initial=data,use_required_attribute=False)
        return render(request, 'interviewtest/complete_signup.html',{'form':form})
    else:
        return redirect(reverse('profile'))


@login_required
@is_signup_complete
def profile(request):
    return render(request,'interviewtest/profile.html',{'client':request.user.clientaccount})
#



@is_approved
def other_info(request):
    try:
        instance = request.user.clientaccount.otherinformation
    except:
        instance = None
    if request.method == 'POST':
        form = OtherInfoForm(request.POST, instance=instance, use_required_attribute=False)
        if form.is_valid():
            other_info = form.save(commit=False)
            if not instance:
                other_info.client = request.user.clientaccount
            other_info.save()
            messages.success(request, 'Account updated successfully')
            return redirect(('profile'))
    else:
        form = OtherInfoForm(instance=instance, use_required_attribute=False)
    return render(request, 'interviewtest/other_info.html', {'form': form})


def auth_error(request):
    return  render(request,'interviewtest/auth_error.html')