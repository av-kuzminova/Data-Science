from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project'),
]
