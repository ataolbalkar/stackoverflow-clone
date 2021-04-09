web: gunicorn stackoverflow_clone.wsgi
worker: celery -A stackoverflow_clone worker --beat -loglevel info