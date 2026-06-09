from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name="index"),
    path('create', views.TaskCreateView.as_view(), name="task_create"),
    path('toggle/<int:pk>/', views.task_toggle, name="task_toggle"),
    path('delete/<int:pk>/', views.task_delete, name="task_delete"),
    path('update/<int:pk>/', views.TaskUpdateView.as_view(), name="task_update"),
]
