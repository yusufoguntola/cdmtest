from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from cdmtest.settings import MIN_PASSWORD_CHARS
from interviewTest.models import ClientAccount, OtherInformation


class ClientAccountForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, label='Surname',widget=forms.TextInput(attrs={'placeholder': 'Surname', 'class': 'form-control'}))
    confirm_password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))
    gender = forms.ChoiceField(choices=(('Male', 'Male'), ('Female', 'Female')), widget=forms.Select(attrs={'class':'form-control'}))
    dob = forms.DateField(input_formats=['%d/%m/%Y', '%d-%m-%Y', '%Y/%m/%d', '%Y-%m-%d'],widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Format: dd/mm/yyyy ,yyyy/mm/dd, dd-mm-yyyy, yyyy-mm-dd'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))

    class Meta:
        model = ClientAccount
        fields = ['last_name','first_name','confirm_password','password','gender','dob']


    def clean_password(self):
        password = str(self.cleaned_data.get('password'))
        confirm_password = str(self.cleaned_data.get('confirm_password'))
        val_errors = []
        if len(password) < MIN_PASSWORD_CHARS:
            val_errors.append(forms.ValidationError(self.error_messages['short_password'], code='short_password'))
        if password != confirm_password:
            val_errors.append(forms.ValidationError(self.error_messages['password_mismatch'], code='password_mismatch'))
        if val_errors:
            raise forms.ValidationError(val_errors)
        return password

    def save(self, commit=True):
        user = User.objects.get(username=self.cleaned_data['username'])
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.set_password(self.cleaned_data['password'])
        user.save()
        user.clientaccount.gender = self.cleaned_data['gender']
        user.clientaccount.DOB = self.cleaned_data['dob']
        user.clientaccount.signup_complete = True
        user.clientaccount.save()
        return user


class OtherInfoForm(forms.ModelForm):

    class Meta:
        model = OtherInformation
        fields = ['home_address','place_of_birth','occupation','phone']

        widgets = {
            'home_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'place_of_birth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

