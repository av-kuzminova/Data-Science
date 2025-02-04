from django.contrib import admin
from django.urls import path, include
from projects.views import home 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), 
    path('users/', include('users.urls')),
    path('projects/', include('projects.urls')),
    path('tasks/', include('tasks.urls')),
]
