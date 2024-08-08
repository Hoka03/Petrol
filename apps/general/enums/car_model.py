from django.db import models


class CarModelChoices(models.TextChoices):
    TOYOTA = 'Toyota', 'Toyota'
    LADA = 'Lada', 'Lada'
    GM = 'GM', 'GM (General Motors)'
    HYUNDAI = 'Hyundai', 'Hyundai'
    NISSAN = 'Nissan', 'Nissan'
    KIA = 'Kia', 'Kia'
    MERCEDES = 'Mercedes', 'Mercedes-Benz'
    BMW = 'BMW', 'BMW'
    RENAULT = 'Renault', 'Renault'
    UAZ = 'UAZ', 'UAZ'
    OPEL = 'Opel', 'Opel'
    JEEP = 'Jeep', 'Jeep'
    CHEVROLET = 'Chevrolet', 'Chevrolet'
