from django.contrib import admin
from .models import Topic
# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id','title','thumbnail','video')

admin.site.register(Topic,TopicAdmin)