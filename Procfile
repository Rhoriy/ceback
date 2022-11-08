web: gunicorn app:app
#worker: celery worker -A tasks.app -l INFO
worker: celery -A tasks.app worker -l INFO
