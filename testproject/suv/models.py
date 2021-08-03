from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Department(models.Model):
    Dept_Name = models.CharField(max_length=30, unique=True)
    Dept_Id=models.IntegerField(primary_key=True)
    Staff_count=models.IntegerField()


class Employee(models.Model):
    Emp_Id=models.IntegerField(primary_key=True)
    Emp_Name=models.CharField(max_length=15,unique=True)
    #Emp_Email=models.EmailField(max_length=30,default="")
    Skills=models.TextField(max_length=40)
    #EDept_Id=models.OneToOneField(Department,on_delete=CASCADE ,related_name="%(class)s_Department")
    EDept_Id=models.ForeignKey(Department,on_delete=CASCADE,related_name='+',null=True,blank=True)


    def __str__(self):
        return str(self.EDept_Id.Dept_Id )
