from django.db import models


class PetrolMarkChoices(models.IntegerChoices):
    OIL_80 = 1, 'Oil 80'
    OIL_90 = 2, 'Oil 90'
    OIL_91 = 3, 'Oil 91'
    OIL_92 = 4, 'Oil 92'
    OIL_95 = 5, 'Oil 95'
    OIL_98 = 6, 'Oil 98'
    OIL_100 = 7, 'Oil 100'
    OIL_101 = 8, 'Oil 101'

    METHANE = 9, 'Methane'
    PROPAN = 10, 'Propan'
    DIESEL = 11, 'Diesel'
    ELECTRIC = 12, 'Electric'
