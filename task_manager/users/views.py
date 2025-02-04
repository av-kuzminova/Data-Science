from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Сразу входим после регистрации
            return redirect("profile")  # Перенаправляем в профиль
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from projects.models import Project
from tasks.models import Task

@login_required
def profile(request):
    user_projects = Project.objects.filter(owner=request.user)  
    user_tasks = Task.objects.filter(executor=request.user)

    return render(request, "users/profile.html", {
        "user_projects": user_projects,
        "user_tasks": user_tasks,
    })
