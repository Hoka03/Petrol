from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

from .validations import phone_validate
from .managers import CustomUserManager
from apps.general.enums.regions import RegionChoices
from apps.general.enums.districts import DistrictChoices


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    username = None
    objects = CustomUserManager()

    phone_number = models.CharField(max_length=13, validators=[phone_validate], unique=True)
    email = models.EmailField(blank=True, null=True)

    region = models.PositiveSmallIntegerField(choices=RegionChoices.choices, blank=True, null=True)
    district = models.PositiveSmallIntegerField(choices=DistrictChoices.choices, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    balance = models.DecimalField(max_digits=10, decimal_places=1, help_text='In UZS', default=0)

    def clean(self):
        if self.district and self.district.split('X')[0] != str(self.region):
            raise ValidationError('Region and District don`t match.')

    def __str__(self):
        return f'{self.phone_number} - {self.email}'

