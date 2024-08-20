from django.conf import settings
from django.db import models
from django.db.models import SET_NULL


class Complaint(models.Model):
    class SectionChoices(models.IntegerChoices):
        STATION = 0
        REVIEW = 1

    class TypeChoices(models.IntegerChoices):
        SPAM = 0
        VIOLENCE = 1
        AUTHOR_RIGHTS = 2
        NARCOTICS = 3
        PERSONAL_INFO = 4
        SCOLD = 5
        OTHERS = 6

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                                blank=True, related_name='complaints')
    station = models.ForeignKey('stations.Station', on_delete=models.SET_NULL, null=True,
                                blank=True, related_name='station')
    review = models.ForeignKey('stations.StationRating', on_delete=SET_NULL, null=True,
                               blank=True, related_name='reviews')

    section = models.PositiveSmallIntegerField(choices=SectionChoices.choices)
    complaint_type = models.PositiveSmallIntegerField(choices=TypeChoices.choices)

    message = models.CharField(max_length=250, blank=True)

    viewed = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)