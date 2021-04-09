web: gunicorn stackoverflow_clone.wsgi
worker: celery -A stackoverflow_clone worker -events -loglevel info
beat: celery -A stackoverflow_clone beat