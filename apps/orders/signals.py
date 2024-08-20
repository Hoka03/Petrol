from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.orders.models import Order


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def update_phone_number(sender, instance, **kwargs):
    Order.objects.filter(user=instance).update(phone_number=instance.phone_number)