from django import forms
from django.forms import widgets
from .models import Department,Employee
from django.forms import ModelChoiceField

class Dep_form(forms.ModelForm):
    class Meta:
        model=Department
        fields=['Dept_Name','Dept_Id','Staff_count']
        widgets={
            'Dept_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Dept_Id': forms.NumberInput(attrs={'class':'form-control'}),
            'Staff_count': forms.NumberInput(attrs={'class':'form-control'}),
        }

class Emp_form(forms.ModelForm):
    
    
    class Meta:
        model=Employee
        fields=['Emp_Id','Emp_Name','Skills','EDept_Id']
        EDept_Id = forms.ModelChoiceField(queryset=Department.objects.values('Dept_Id'))
        widgets={
            'Emp_Id': forms.NumberInput(attrs={'class':'form-control'}),
            'Emp_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Skills': forms.Textarea(attrs={'class':'form-control'}),
            #'EDept_Id' : forms.ChoiceField(attrs={'choices': type_choices}),
            #'EDept_Id' : forms.ModelChoiceField(queryset=Department.objects.all())
        }

    
    def __init__(self, *args, **kwargs):
        super(Emp_form, self).__init__(*args, **kwargs)

        self.fields['EDept_Id'].label_from_instance = self.label_from_instance

    @staticmethod
    def label_from_instance(obj):
        return obj.Dept_Id
    """def __init__(self, *args, **kwargs):
        EDept_Id = kwargs.pop('EDept_Id', None)
        super(Emp_form, self).__init__(*args, **kwargs)

        if EDept_Id:
            self.fields['adminuser'].queryset = Department.objects.filter(account=Employee.EDept_Id)

#form = Emp_form(EDept_Id=3)


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "My Object #%i" % obj.id
        
        def __init__(self,*args,**kwargs):
            super(Emp_form, self).__init__(*args, **kwargs)
            print("==================================")
            print(Department.objects.values('Dept_Id'))
            print("==================================")
            print(Department.objects.values('Dept_Id').distinct())
            print("==================================")
            #type_choices = [(i['Dept_Id']) for i in Department.objects.values('Dept_Id').distinct()]
            self.fields['EDept_Id'] = forms.ChoiceField(
            choices=[o for o in Department.objects.values('Dept_Id')]
        )
       def __init__(self, *args, **kwargs):
            super(Emp_form, self).__init__(*args, **kwargs)
            self.fields['EDept_Id'].choices = Department.objects.all().values_list('Dept_Id')
            #self.fields['EDept_Id'].queryset = Department.objects.all().values('Dept_Id')
        #'EDept_Id': forms.ChoiceField(attrs={'class':'form-control'}),"""
            
   # type = forms.ChoiceField(choices=type_choices)
     #'EDept_Id': forms.NumberInput(attrs={'class':'form-control'}),


     

