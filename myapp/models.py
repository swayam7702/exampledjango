from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(max_length=200)
    is_active = models.BooleanField(default=True)
    profile_pic = models.ImageField(upload_to='images')
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True) 
    # city = models.CharField(max_length=50)
 


    class Meta:
      
        verbose_name = 'Student'
        verbose_name_plural = 'Students'