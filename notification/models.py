from django.contrib.auth import get_user_model
from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True)
    date = models.DateTimeField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
