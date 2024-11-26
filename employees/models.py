from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField()
    role = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now_add=False)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50) 
    company_location = models.CharField(max_length=50,default="Hyderabad") 
    qualification = models.CharField(max_length=50,default="")

    

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'