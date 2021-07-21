from django.shortcuts import render ,HttpResponseRedirect
from .forms import StudentRegestration
from .models import User
# Create your views here.

#This function will add new items and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegestration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em)
            #fm.save()
            reg.save()
            fm = StudentRegestration()
    else :
        fm = StudentRegestration()
    stud=User.objects.all()
    context={'form':fm,'stud':stud}
    return render(request,'enroll/addandshow.html',context)

#This function will delete
def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request, id):
    if request.method=="POST":
        pi = User.objects.get(pk=id)
        fm=StudentRegestration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegestration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})
