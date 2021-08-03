from suv.models import Department, Employee
from django.contrib import admin

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('Dept_Name','Dept_Id','Staff_count')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('Emp_Id','Emp_Name','Skills','EDept_Id')