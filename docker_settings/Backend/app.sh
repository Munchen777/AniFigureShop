#!bin/bash

cd /app/anifigure

echo "Running Django setup tasks..."
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

echo "Creating superuser..."
python manage.py shell << EOF
from django.contrib.auth import get_user_model
from django.core.management import call_command

User = get_user_model()
if not User.objects.filter(email="${DJANGO_SUPERUSER_EMAIL}").exists():
    User.objects.create_superuser(
        email="${DJANGO_SUPERUSER_EMAIL}",
        password="${DJANGO_SUPERUSER_PASSWORD}",
    )
EOF
echo "Superuser ${DJANGO_SUPERUSER_LOGIN} is created..."

gunicorn --bind 0.0.0.0:8000 anifigure.wsgi:application
