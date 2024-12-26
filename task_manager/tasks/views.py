from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Project
from .forms import TaskForm, ProjectForm

# Главная страница с задачами
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Страница проекта с задачами
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tasks = project.tasks.all()
    return render(request, 'tasks/project_detail.html', {'project': project, 'tasks': tasks})

# Создание новой задачи
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

# Создание нового проекта
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = ProjectForm()
    return render(request, 'tasks/project_form.html', {'form': form})

