#!/usr/bin/env sh

python manage.py migrate
gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers 3 --reload
