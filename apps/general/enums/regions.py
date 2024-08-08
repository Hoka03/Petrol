from django.db import models


class RegionChoices(models.IntegerChoices):
    ANDIJON = 1, 'Andijon'
    BUXORO = 2, 'Buxoro'
    FARGONA = 3, 'Farg‘ona'
    JIZZAX = 4, 'Jizzax'
    XORAZM = 5, 'Xorazm'
    NAMANGAN = 6, 'Namangan'
    NAVOIY = 7, 'Navoiy'
    QASHQADARYO = 8, 'Qashqadaryo'
    SAMARQAND = 9, 'Samarqand'
    SIRDARYO = 10, 'Sirdaryo'
    SURXONDARYO = 11, 'Surxondaryo'
    TOSHKENT = 12, 'Toshkent'
    QORAQALPOGISTON = 13, 'Qoraqalpog‘iston Respublikasi'
