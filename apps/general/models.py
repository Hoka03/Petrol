from django.db import models


class General(models.Model):
    booking_price = models.PositiveIntegerField(default=0)

    min_payment_amount = models.PositiveIntegerField()

    @classmethod
    def get_booking_price(cls):
        return getattr(cls.objects.first(), 'booking_price', 0)

    @classmethod
    def get_min_payment_amount(cls):
        return getattr(cls.objects.first(), 'min_payment_amount', 5000)