# tasks/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Task
from .constants import SORT_OPTION

def index(request):
    tasks = Task.objects.all()
    search = request.GET.get("search", "")

    if search:
        tasks = tasks.filter(title__icontains = search)
    
    tasks = get_sorted_task(request=request)

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


    context = {
        "tasks": tasks,
        "sorts": SORT_OPTION,
        "tomorrow": timezone.now() + timedelta(days=1),
    }

    if request.htmx:
        return render(
            request=request,
            template_name = "tasks/task_list.html",
            context=context
        )
    return render(
        request = request,
        context = context,
        template_name= 'tasks/tasks.html'
    )

def get_sorted_task(request):
    tasks = Task.objects.all()
    selected_sort = request.GET.get("sort", "")
    if selected_sort in SORT_OPTION:
        tasks = tasks.order_by(
            SORT_OPTION[selected_sort]
        )
    return tasks

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
