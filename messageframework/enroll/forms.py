from django import forms
from .models import Userloginmodel

class Userloginform(forms.ModelForm):
    class Meta:
        model = Userloginmodel
        fields= "__all__"
