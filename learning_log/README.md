
- python3 -m venv ll_env
- source ll_env/bin/activate
- pip install Django
- django-admin.py startproject learning_log .
- python manage.py migrate
- python manage.py runserver
- python manage.py startapp learning_logs
- python manage.py makemigrations learning_logs
- python manage.py createsuperuser
