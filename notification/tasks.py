from datetime import timedelta

from django.core.mail import send_mail
from django.utils import timezone

from notify_server.celery import app
from notification.models import Notification


@app.task(name='send_notifications')
def send_notifications(notify_id):
    notification = Notification.objects.get(id=notify_id)
    send_mail(
        notification.title,
        notification.description,
        'notify_email@gmail.com',
        [notification.owner.email, ],
        fail_silently=False,
    )


@app.task(name='check_notifications')
def check_notifications():
    print(timezone.now() + timedelta(minutes=60))
    notify_ids = [obj.id for obj in Notification.objects.filter(
        date__range=(timezone.now() + timedelta(minutes=59), timezone.now() + timedelta(minutes=60)),
    )]
    for notify_id in notify_ids:
        send_notifications.delay(notify_id)
