from django.db import models


class CarCategory(models.TextChoices):
    SEDAN = 'Sedan', 'Sedan'
    SUV = 'SUV', 'SUV'
    HATCHBACK = 'Hatchback', 'Hatchback'
    PICKUP = 'Pickup', 'Pickup'
    COUPE = 'Coupe', 'Coupe'
    CONVERTIBLE = 'Convertible', 'Convertible'
    MINIVAN = 'Minivan', 'Minivan'
    WAGON = 'Wagon', 'Wagon'
    CROSSOVER = 'Crossover', 'Crossover'
    VAN = 'Van', 'Van'
