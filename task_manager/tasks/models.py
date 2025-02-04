from django.db import models
from django.contrib.auth import get_user_model
from projects.models import Project

User = get_user_model()

class Task(models.Model):
    STATUS_CHOICES = [
        ("to_do", "В работу"),
        ("in_progress", "В работе"),
        ("done", "Выполнен"),
        ("cancelled", "Отменен"),
    ]

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="to_do")
    estimated_hours = models.FloatField(verbose_name="Оценка в часах", blank=True, null=True)
    attachment = models.TextField(verbose_name="Текстовое вложение", blank=True, null=True)

    def __str__(self):
        return self.title
