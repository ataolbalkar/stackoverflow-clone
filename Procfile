web: gunicorn stackoverflow_clone.wsgi
worker: celery -A stackoverflow_clone worker -l info
beat: celery -A stackoverflow_clone beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler