import os


CELERY_TASK_SERIALIZER = 'json'
BROKER_URL =  os.environ.get('REDISGREEN_URL', 'redis://localhost:6379/0')
#BROKER_URL =  os.environ.get('redis://localhost:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
#CELERY_RESULT_BACKEND = 'redis://'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

#CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
