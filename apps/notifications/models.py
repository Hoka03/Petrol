from django.conf import settings
from django.db import models


class NotificationType(models.Model):
    class Type(models.IntegerChoices):
        DISCOUNT = 0
        ON_BOOKING = 1
        REMIND = 2
        MAINTENANCE_DUE = 3
        SAFETY_ALERT = 4

    section = models.PositiveIntegerField(choices=Type.choices, unique=True)
    image = models.ImageField(upload_to='notification/images/')


class Notification(models.Model):
    section = models.PositiveIntegerField(choices=NotificationType.Type.choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
