from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_projects")
    members = models.ManyToManyField(User, related_name="projects", blank=True)

    def __str__(self):
        return self.name
