from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator

from apps.general.models import General
from apps.stations.models import Station
from apps.cars.models import Car
from apps.general.enums.petrol_mark import PetrolMarkChoices


class Booking(models.Model):
    station = models.ForeignKey(Station, on_delete=models.PROTECT)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    car_number = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)

    petrol_mark = models.PositiveSmallIntegerField(choices=PetrolMarkChoices.choices)

    quantity = models.PositiveSmallIntegerField()
    booking_time = models.DateTimeField(validators=[MinValueValidator(now)])
    minutes = models.PositiveSmallIntegerField(help_text='In minutes')

    def save(self, *args, **kwargs):
        if not self.car_number:
            self.car_number = self.car.number
        if not self.car_model:
            self.car_number = self.car.model

        if not self.pk:
            user = self.car.user
            user.balance = max(user.balance - getattr(General.get_booking_price(), 'booking_price', 0), 0)
            user.save()
        return super().save(*args, **kwargs)