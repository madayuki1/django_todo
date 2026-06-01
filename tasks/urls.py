from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('toggle/<int:pk>/', views.toggle_task, name="toggle_task"),
    path('delete/<int:pk>/', views.delete_task, name="delete_task"),
    path('edit/<int:pk>/', views.TaskEdit.as_view(), name="edit_task"),
]
