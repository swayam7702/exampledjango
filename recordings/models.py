from django.db import models

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.FileField(upload_to="images/")
    video =  models.FileField(upload_to="videos/")


    

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'