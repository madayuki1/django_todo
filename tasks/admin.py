from django.contrib import admin
from .models import Task

admin.site.site_header = 'Our Django'
# Register your models here.
# @admin.register(Task)
# class TaskAdmin(admin.ModelAdmin):
#     fields = ['title', 'completed']

admin.site.register(Task)