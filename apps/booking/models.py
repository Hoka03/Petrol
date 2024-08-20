from django.conf import settings
from django.db import models
from django.db.models import SET_NULL, PROTECT
from django.utils.timezone import now
from django.core.validators import MinValueValidator
from kombu.common import PREFETCH_COUNT_MAX

from apps.general.models import General
from apps.stations.models import Station
from apps.cars.models import Car
from apps.general.enums.petrol_mark import PetrolMarkChoices


class Booking(models.Model):
    station_petrol_mark = models.ForeignKey(to='stations.StationPetrolMark', on_delete=SET_NULL, null=True)
    station = models.ForeignKey(Station, on_delete=SET_NULL, null=True)
    petrol_mark = models.PositiveSmallIntegerField(choices=PetrolMarkChoices.choices)

    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    car_number = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)

    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    booking_time = models.DateTimeField(validators=[MinValueValidator(now)])

    minutes = models.PositiveSmallIntegerField(help_text='In minutes', editable=False)

    def save(self, *args, **kwargs):
        if not self.car_number:
            self.car_number = self.car.number
        if not self.car_model:
            self.car_number = self.car.model

        if not self.station_id:
            self.station_id = self.station_petrol_mark.station_id
        if not self.petrol_mark:
            self.petrol_mark = self.station_petrol_mark.petrol_marks

        if not self.minutes:
            self.minutes = (round(
                self.station_petrol_mark.fill_time * self.quantity / 60, 0
            ) + General.get_booking_extra_time())

        if not self.pk:
            user = self.car.user
            user.balance = max(user.balance - getattr(General.get_booking_price(), 'booking_price', 0), 0)
            user.save()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.car} - {self.station}"