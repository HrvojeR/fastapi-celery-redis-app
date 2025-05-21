from celery import Celery
from settings import REDIS_URL
from celery.schedules import schedule
from celery.schedules import crontab

celery_app = Celery(
    'celery_worker',
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["tasks"]
)

from datetime import timedelta

celery_app.conf.beat_schedule = {
    'print-random-item-every-5-seconds': {
        'task': 'tasks.insert_random_item',
        'schedule': crontab(hour=14, minute=45),
    },
}

celery_app.conf.timezone = 'Europe/Sarajevo'
