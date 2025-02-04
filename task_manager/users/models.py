from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Здесь можешь добавить дополнительные поля для пользователя, если нужно
    role = models.CharField(max_length=50, blank=True, null=True)

    # Добавляем related_name для избегания конфликта с группами и разрешениями
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Указываем уникальное имя для обратной связи
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Указываем уникальное имя для обратной связи
        blank=True
    )
