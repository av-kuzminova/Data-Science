from django.shortcuts import render

def project_list(request):
    # Пример: выводим список проектов (пока просто пример)
    return render(request, 'projects/project_list.html')

from django.shortcuts import render

def home(request):
    return render(request, 'projects/home.html')  # Путь к шаблону главной страницы
