from django.db import models
from django.conf import settings

from apps.stations.models import Station


class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
