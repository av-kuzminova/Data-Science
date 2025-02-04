from django.contrib import admin
from .models import Project

# Регистрируем модель проекта
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')  # Показываем название проекта и владельца
    search_fields = ('name',)  # Поиск по названию проекта
    list_filter = ('owner',)  # Фильтрация по владельцу проекта
