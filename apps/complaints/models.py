from django.db import models


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

    section = models.PositiveSmallIntegerField(choices=SectionChoices.choices)
    complaint_type = models.PositiveSmallIntegerField(choices=TypeChoices.choices)
    message = models.CharField(max_length=250, blank=True)
    viewed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)