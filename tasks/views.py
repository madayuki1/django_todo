# tasks/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task

def tasks(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }

    return render(
        request = request,
        context = context,
        template_name= 'tasks/tasks.html'
    )