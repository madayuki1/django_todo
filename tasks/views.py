# tasks/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Task

def index(request):

    if request.method == "POST":
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")

        if title:
            Task.objects.create(
                title=title,
                due_date=due_date
            )

        return redirect(
            to='index'
        )

    tasks = Task.objects.all()

    context = {
        "tasks": tasks,
        "tomorrow": timezone.now() + timedelta(days=1),
    }

    return render(
        request = request,
        context = context,
        template_name= 'tasks/tasks.html'
    )

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect(
        to='index'
    )

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect(
        to='index'
    )