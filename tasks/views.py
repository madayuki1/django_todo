# tasks/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from django import forms
from django.views.generic import UpdateView, ListView, CreateView
from datetime import timedelta
from .models import Task
from .constants import SORT_OPTION, DEFAULT_SORT

class TaskListView(ListView):
    model = Task
    template_name = "tasks/tasks.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.hide_completed = self.request.GET.get("hide-completed")
        self.search = self.request.GET.get('search-list')
        self.selected_sort = self.request.GET.get('sort-list', DEFAULT_SORT)

        if self.hide_completed:
            queryset = queryset.filter(completed=False)
        
        if self.search:
            queryset = queryset.filter(title__icontains=self.search)
        
        queryset = get_sorted_task(queryset, self.selected_sort)
        
        return queryset    

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["sorts"] = SORT_OPTION
        context["form"] = TaskForm
        context["hide_completed"] = self.hide_completed
        context["selected_sort"] = self.selected_sort
        context["search"] = self.search
        return context
    
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            
        return redirect('index')

class TaskForm(forms.ModelForm):
    """Form definition for Task."""

    class Meta:
        """Meta definition for Taskform."""

        model = Task
        fields = ('title', "due_date")

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "type": "text"
                }
            ),
            "due_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            )
        }

class TaskCreateView(CreateView):
    model = Task
    # fields = ['title', 'due_date']
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("index")

class TaskUpdateView(UpdateView):
    model = Task
    # fields = ['title', 'due_date']
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("index")

def get_sorted_task(tasks, selected_sort):
    if selected_sort in SORT_OPTION:
        tasks = tasks.order_by(
            SORT_OPTION[selected_sort]["keyword"]
        )
    return tasks

def task_toggle(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect(
        to='index'
    )

def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect(
        to='index'
    )
