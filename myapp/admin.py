from django.contrib import admin
from .models import Student
# Register your models here.

# class studentAdmin(admin.ModelAdmin):
    
class StudentAdmin(admin.ModelAdmin):
    list_display=('name','age','address','created_at')

admin.site.register(Student,StudentAdmin)

