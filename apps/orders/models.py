from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now

from apps.general.models import General
from config import settings


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField()
    is_paid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        if not self.pk and self.amount < General.get_min_payment_amount():
            raise ValidationError({'amount': 'min amount price mistake.'})

    def save(self, *args, **kwargs):
        if self.is_paid and not self.paid_at:
            self.paid_at = now()
        return super().save(*args, **kwargs)