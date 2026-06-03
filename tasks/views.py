# tasks/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView
from datetime import timedelta
from .models import Task
from .constants import SORT_OPTION, DEFAULT_SORT

def index(request):
    tasks = Task.objects.all()
    search = request.GET.get("search", "")
    selected_sort = request.GET.get("sort", DEFAULT_SORT)
    hide_completed = request.GET.get("hide-completed", "")

    if search:
        tasks = tasks.filter(title__icontains = search)
    
    if hide_completed:
        tasks = tasks.filter(completed = False)
    
    tasks = get_sorted_task(tasks = tasks, selected_sort=selected_sort)

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
        "selected_sort": selected_sort,
        "hide_completed": hide_completed,
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


class TaskListView(ListView):
    model = Task
    template_name = "tasks/tasks.html"

    def get_queryset(self):
        return super().get_queryset()
    

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["sorts"] = SORT_OPTION
        return context
    

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'due_date']
    template_name = "tasks/task_edit.html"
    success_url = reverse_lazy('index')

def get_sorted_task(tasks, selected_sort):
    if selected_sort in SORT_OPTION:
        tasks = tasks.order_by(
            SORT_OPTION[selected_sort]["keyword"]
        )
    return tasks

def toggle_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect(
        to='index'
    )

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect(
        to='index'
    )
