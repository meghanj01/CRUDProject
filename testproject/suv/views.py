from suv.models import Department, Employee
from django.shortcuts import render ,HttpResponseRedirect
from .forms import Dep_form,Emp_form
from django.contrib import messages
import re
# Create your views here.
def home(request):
    return render(request,'suv/home.html')
def mock(request):
    return render(request,'suv/dataview.html')
def add_show(request,table):
    if table== "Dep_form":
        cur_models= Department
        cur_forms= Dep_form
    elif table  == "Emp_form":
        cur_models= Employee
        cur_forms= Emp_form

    if request.method=="POST":

        fm=cur_forms(request.POST)
        #print("*******************************")
        #print("formobject"+str(fm))
        if fm.is_valid():
                if table == "Dep_form":
                    print(fm.cleaned_data['Dept_Name'])
                    fm.save()
                    
                    # uname=fm.cleaned_data['Dept_Name']
                    # uid=fm.cleaned_data['Dept_Id']
                    # ustaff=fm.cleaned_data['Staff_count']
                    # user=Department(Dept_Name=uname,Dept_Id=uid,Staff_count=ustaff)
                    messages.success(request,"Congratulations !! You added a new department")
                if table == "Emp_form":
                    #print(fm.cleaned_data['EDept_Id'].Dept_Id)
                    fm.save()
                    # uid=fm.cleaned_data['Emp_Id']
                    # uname=fm.cleaned_data['Emp_Name']
                    # uskills=fm.cleaned_data['Skills']
                    # uemp_dept=fm.cleaned_data['EDept_Id']
                    
                    # user=Employee(Emp_Id=uname,Emp_Name=uname,Skills=uskills,EDept_Id=uemp_dept)
                    messages.success(request,"Congratulations !! You added a new Employee")
    else:
        fm=cur_forms()
        #print("formobject"+str(fm))
    # if searchval:
    #     values=cur_models.objects.filter(Dept_Name=searchval)
    # else:

    values=None
    try :
        print(request.POST.get('searchvalue'))

        #print(re.fullmatch('^[0-9]+$',request.POST.get('searchvalue')))
        if re.fullmatch('^[0-9]+$',str(request.POST.get('searchvalue'))) :
            print("Reaching here")
            #print(request.POST.get('searchvalue').value())
            id=request.POST.get('searchvalue')
            values=cur_models.objects.filter(pk=id)
            print("Reaching out")
            print(values)
    except AttributeError:
        pass
    if  request.POST.get('DSC')=="DSC"  :
        print("Inside DESC")
        print(values)
        values=cur_models.objects.order_by('-Dept_Id')
    elif request.POST.get('ASC')=="ASC" and re.fullmatch('^[0-9]+$',request.POST.get('searchvalue'))   :
        print("Inside ASC")
        print(values)
        id=request.POST.get('searchvalue')
        values=cur_models.objects.filter(pk=id)
    elif request.POST.get('ASC')=="ASC" and not (re.fullmatch('^[0-9]+$',request.POST.get('searchvalue')) )  :
        values=cur_models.objects.order_by('Dept_Id')
        print(values)
    print("printing values")
    print(values)
    #print( "length of values"+str(len(values)) )
    if not values :
        values=cur_models.objects.all()

    
    
        

    
       
    print("**************************8")
    print(values)
    context={'forms':fm ,'values':values}

    return render (request,'suv/Dashboard_'+table+'.html',context)

def delete_date(request,id,table):
    if table == "Dep_form":
        cur_models= Department
        cur_forms= Dep_form
    elif table == "Emp_form":
        cur_models= Employee
        cur_forms= Emp_form    
    if request.method=="POST":
        data=cur_models.objects.get(pk=id)
        data.delete()
        messages.success(request,"Congratulations !! You deleted a row")
    return HttpResponseRedirect('/Dashboard/'+table)

def update_data(request,id,table):
    if table == "Dep_form":
        cur_models= Department
        cur_forms= Dep_form
    elif table == "Emp_form":
        cur_models= Employee
        cur_forms= Emp_form   
    print(cur_models)
    print(Department)
    data=cur_models.objects.get(pk=id) 
    if request.method=="POST":
        fm=cur_forms(request.POST,instance=data)
        if fm.is_valid():
            
            fm.save()
            messages.success(request,"Congratulations !! You updated new row")
    else:
        fm=cur_forms(instance=data)
    return render(request,'suv/updates_'+table+'.html',{'form':fm})