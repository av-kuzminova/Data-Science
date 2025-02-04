from django.contrib import admin
from .models import CustomUser

# Регистрируем модель пользователя
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')  # Показываем эти поля в списке пользователей
    search_fields = ('username', 'email')  # Поиск по этим полям
    list_filter = ('role',)  # Фильтрация по роли
