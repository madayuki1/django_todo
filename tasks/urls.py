from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name="index"),
    path('toggle/<int:pk>/', views.toggle_task, name="toggle_task"),
    path('delete/<int:pk>/', views.delete_task, name="delete_task"),
    path('edit/<int:pk>/', views.TaskUpdateView.as_view(), name="edit_task"),
]
