from django.db import models
from django.contrib.auth.models import User

# Модель проекта
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Модель задачи
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='new')
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

