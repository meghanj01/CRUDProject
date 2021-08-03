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
 


     

