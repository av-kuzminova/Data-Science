# from django.contrib.auth import views as auth_views
# from django.contrib import admin
# from django.urls import path, include
# from django.shortcuts import redirect

# def redirect_to_login(request):
#     return redirect('login')  # Перенаправление на login

# urlpatterns = [
#     path('', redirect_to_login, name='home'),  # Главная страница перенаправляет на login
#     path('admin/', admin.site.urls),
#     path('', include('todolist.urls')),
#     path('login/', auth_views.LoginView.as_view(), name='login'),
#     path('logout/', redirect_to_login, name='home'),
#     path('users/', include('users.urls')),  # Подключаем маршруты из users
#     path('todolist/', include('todolist.urls')),
#     path('', include('django.contrib.auth.urls')),
#     path('login/', include('django.contrib.auth.urls')),  # Встроенные маршруты авторизации
# ]

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from users import views  # Добавляем импорт представлений из users

def redirect_to_login(request):
    return redirect('login')  # Перенаправление на login

urlpatterns = [
    path('', redirect_to_login, name='home'),  # Главная страница перенаправляет на login
    path('admin/', admin.site.urls),
    path('todolist/', include('todolist.urls')),  # Подключаем маршруты для todolist
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Стандартная страница входа
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Стандартный выход
    path('register/', views.register, name='register'),  # Прямой путь к представлению регистрации
    # path('users/', include('users.urls')),  # Подключаем другие маршруты пользователей
]



