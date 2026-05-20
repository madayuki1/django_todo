# tasks/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):

    if request.method == "POST":
        title = request.POST.get("title")

        if title:
            Task.objects.create(title=title)

        return redirect(
            to='index'
        )

    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }

    return render(
        request = request,
        context = context,
        template_name= 'tasks/tasks.html'
    )

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return task