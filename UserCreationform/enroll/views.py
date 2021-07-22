from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registration
# Create your views here.
def login(request):
    if request.method=="POST":
        fm=registration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Saved successfully !!!")

    else:
        fm=registration()
    return render(request,'enroll/registration.html',{'form':fm})
