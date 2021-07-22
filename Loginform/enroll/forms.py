from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm
from django import forms

class registration(UserCreationForm):
    #password2=forms.CharField(label="Confirm password (again)",widget=forms.PasswordInput)
    class Meta:
        model= User
        fields=['username','first_name','last_name','email']
        labels={'email':'EMail'}

class editUserProfile(UserChangeForm):
    password=None
    class Meta:
        model= User
        fields=['username','first_name','last_name','email','date_joined','last_login','is_active']
        labels={'email':'Email'}
