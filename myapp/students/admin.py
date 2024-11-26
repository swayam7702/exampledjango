from django.contrib import admin
from .models import Stud
# Register your models here.

class StudAdmin(admin.ModelAdmin):
    list_display = ('id','name','addres','course','joinedDate','is_active','dob')
    list_display_links = ('name',)
    list_filter = ('course','addres','is_active')


admin.site.register(Stud,StudAdmin)