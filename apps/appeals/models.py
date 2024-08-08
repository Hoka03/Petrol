from django.db import models
from django.conf import settings

from apps.users.validations import phone_validate


class Appeal(models.Model):
    class Section(models.IntegerChoices):
        STATION_CREATOR = 0
        TECHNICAL_SUPPORT = 1

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=13, validators=[phone_validate], blank=True, null=True)
    section = models.PositiveIntegerField(choices=Section.choices)
    message = models.CharField(max_length=250, blank=True)
