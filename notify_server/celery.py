import os
from celery import Celery
from datetime import timedelta

from notify_server.settings import CELERYBEAT_SCHEDULE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notify_server.settings')

app = Celery('notify_server')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.update(CELERYBEAT_SCHEDULE=CELERYBEAT_SCHEDULE)

