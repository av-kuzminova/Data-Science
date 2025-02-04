from rest_framework import serializers
from .models import Task
from projects.models import Project
from users.models import CustomUser

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'executor', 'project', 'status', 'estimated_hours', 'attachment']
