from django.db import models
from django.conf import settings
from django.core.validators import ValidationError
from django.contrib.postgres.fields import ArrayField

from .validations import CarNumberValidator
from apps.general.enums.petrol_mark import PetrolMarkChoices


class CarModel(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    parent = models.ForeignKey('self', on_delete=models.PROTECT)

    def clean(self):
        if not self.pk and self.parent.parent.parent:
            raise ValidationError({'parent': 'Create only 3 degree category in parent field.'})


class Car(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    model = models.ForeignKey(to=CarModel, on_delete=models.PROTECT)

    number = models.CharField(max_length=8, validators=[CarNumberValidator], unique=True)
    color = models.CharField(max_length=50)
    petrol_mark = ArrayField(models.CharField(choices=PetrolMarkChoices.choices))

    def clean(self):
        if not self.model.parent.parent:
            raise ValidationError({'model': 'Choose Third degree category'})

    def __str__(self):
        return f'{self.user} - {self.number}'

