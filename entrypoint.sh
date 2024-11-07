#!/bin/bash

# Parse the server type argument (WEB, MIGRATE, COLLECTSTATIC, etc.)
server="_"
while getopts s: flag; do
    case "${flag}" in
        s) server=${OPTARG};;  # Capture the server type passed with -s option
    esac
done

if [ "$server" = "WEB" ]; then
    echo "Starting Gunicorn for the website..."
    gunicorn ytprj.wsgi:application --bind 0.0.0.0:8000 --workers 4 ${@:3}
elif [ "$server" = "MIGRATE" ]; then
    echo "Applying database migrations..."
    python manage.py migrate ${@:3}
elif [ "$server" = "COLLECTSTATIC" ]; then
    echo "Collecting static files for production..."
    python manage.py collectstatic --noinput
else
    echo "Running custom command: $@"
    exec "$@"
fi

