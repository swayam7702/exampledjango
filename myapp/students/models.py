from django.db import models

# Create your models here.

class Stud(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    addres = models.CharField(max_length=50)
    dob = models.DateField()
    joinedDate = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
   

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Stud'
        verbose_name_plural = 'Studs'



class Sample(models.Model):

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Sample'
        verbose_name_plural = 'Samples'