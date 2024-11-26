from django.contrib import admin
from .models import Employee
# Register your models here.


class EmployeeDetails(admin.ModelAdmin):
    list_display = ('emp_id','name','role','city','date_joined','company_name')


admin.site.register(Employee,EmployeeDetails)