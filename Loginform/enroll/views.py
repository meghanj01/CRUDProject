from django.shortcuts import render ,HttpResponseRedirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registration
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate ,login ,logout
# Create your views here.
#signup view function
def signup(request):
    if request.method=="POST":
        fm=registration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Saved successfully !!!")

    else:
        fm=registration()
    return render(request,'enroll/registration.html',{'form':fm})

#login view function
def user_login(request):
    if request.user.is_authenticated:
        return  HttpResponseRedirect('/profile/')
    else:
        if request.method =="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user :
                    login(request,user)
                    messages.success(request,"Logged in successfully")
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':fm})


def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
