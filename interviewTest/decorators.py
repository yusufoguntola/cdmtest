from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def is_approved(function):
    def wrap(request, *args, **kwargs):
        try:
            s =request.user.clientaccount.is_approved
            return function(request, *args, **kwargs)
        except:
            messages.error(request,'Permission denied. Your account is not approved yet.')
            return redirect('home')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_superuser(function):
    def wrap(request, *args, **kwargs):
        try:
            if request.user.is_superuser:
                return function(request, *args, **kwargs)
            else:
                messages.error(request, 'Admin Access Violation.')
                return redirect('home')
        except:
            messages.error(request,'Permission denied.')
            return redirect('home')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap



def is_signup_complete(function):
    def wrap(request, *args, **kwargs):
        try:
            if request.user.clientaccount.signup_complete:
                return function(request, *args, **kwargs)
            else:
                messages.error(request,
                               'Permission denied. You need to complete your registration. Login again to do so')
                return redirect('logout')
        except:
            messages.error(request,'Permission denied.')
            return redirect('home')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
