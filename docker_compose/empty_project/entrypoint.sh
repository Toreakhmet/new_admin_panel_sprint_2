#!/bin/sh

while ! nc -z db 5432; do
  sleep 0.1
done

python manage.py collectstatic --no-input
python manage.py migrate --no-input
python manage.py loaddata data.json

uwsgi --http :8000 --chdir /opt/app --module config.wsgi:application

exec "$@"