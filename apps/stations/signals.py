from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.stations.models import Station, StationRating


@receiver(post_save, sender=Station)
def update_station_rating(instance, created, *args, **kwargs):
    if created:
        instance.station.rating = StationRating.objects.aggregate(r=models.Avg('rating'))['r']
        instance.station.save()

