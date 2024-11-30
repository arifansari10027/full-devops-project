from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  # Update the path if needed
]
