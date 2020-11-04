release: python manage.py check
release: python manage.py migrate
release: python manage.py collectstatic --no-input
web: gunicorn main.wsgi --log-file -
