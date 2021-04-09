web: gunicorn stackoverflow_clone.wsgi
main_worker: celery -A stackoverflow_clone worker --beat -Q uw -l info --without-gossip --without-mingle --without-heartbeat