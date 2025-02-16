Простой ToDo менеджер, реализованный на веб-фреймворке Django
В качестве веб-интерфейса использован фреймворк Semantic UI https://semantic-ui.com/

Создаем папку для нового проекта и переходим в нее

    md ToDoDjango & cd ToDoDjango


Устанавливаем и активируем виртуальное окружение

    python3 -m venv venv
    . venv/bin/activate


Инициализируем git

    git init


Устанавливаем модули

    pip install django gunicorn


Создаем проект todoapp и переходим в него

    django-admin startproject todoapp & cd todoapp

Создадим приложение todolist

    python manage.py startapp todolist

Зарегистрируем приложение в файле settings.py

    INSTALLED_APPS = [
    ...,
    todolist,
]

Укажем локализацию и часовой пояс в файле settings.py

    LANGUAGE_CODE = 'ru-ru'
    TIME_ZONE = 'Europe/Moscow'

Добавим папку шаблонов в settings.py

    TEMPLATES = [
    {...,
    'DIRS': ['templates'],
    }]

Структура файлов и папок

    md templates
    mkdir todolist\static\css
    echo .> .gitignore
    echo .> templates/layout.html
    echo .> templates/index.html
    echo .> todolist/static/todolist/css/style.css
    echo .> README.MD
    echo .> todolist/urls.py


Подтянем всю статику в папку static нашего проекта

    python manage.py collectstatic

Создаем файл с зависимостями проекта

    pip freeze > requirements.txt


Запускаем сервер

    python manage.py runserver


В проекте так же присутствуют файл Procfile и runtime.txt, для публикации проекта на heroku.com

База данных должна быть в файле .gitignore, но для этого примера я ее оттуда удалил, чтобы был пример ToDo задач

Ссылка на оригинал: https://youtu.be/3vfum74ggHE
    
    Терехов Михаил 2022 год