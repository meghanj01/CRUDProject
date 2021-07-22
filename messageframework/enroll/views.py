from django.shortcuts import render
from .models import Userloginmodel
from .forms import Userloginform
from django.contrib import messages
# Create your views here.
def Userlogin(request):
    if request.method=="POST":
        fm=Userloginform(request.POST)
        if fm.is_valid():
            fm.save()
            print(messages.get_level(request))
            messages.set_level(request,messages.DEBUG)
            messages.info(request,"Your account is successfully created !!!")
            messages.error(request,"Your account is successfully created !!!")
            messages.success(request,"Your account is successfully created !!!")
            messages.warning(request,"Your account is successfully created !!!")
            messages.debug(request,"Your account is successfully created !!!")
    else:
        fm=Userloginform()
    return render(request,'enroll/login.html',{'form':fm})
