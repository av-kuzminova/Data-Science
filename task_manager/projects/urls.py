from django.urls import path
from . import views

app_name = 'projects'  # Добавляем пространство имен для маршрутов этого приложения

urlpatterns = [
    path('', views.project_list, name='project_list'),  
    path('', views.home, name='home'),
]

