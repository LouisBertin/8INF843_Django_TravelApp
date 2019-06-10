#!/usr/bin/env bash
while ! pg_isready -h db -p 5432 > /dev/null 2> /dev/null; do
echo "Connecting to db Failed"
sleep 1
done

echo "Apply database migrations"
python manage.py migrate

echo "Starting server"
gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers 3 --reload
