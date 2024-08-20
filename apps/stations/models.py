from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.postgres.fields import ArrayField

from apps.general.enums.petrol_mark import PetrolMarkChoices
from apps.general.enums.week_day import WeekDayChoices


class Station(models.Model):
    class Comforts(models.IntegerChoices):
        MOSQUE = 1, 'Mosque'
        PARK = 2, 'Park'
        GYM = 3, 'Gym'
        SHOPPING_MALL = 4, 'Shopping Mall'
        WC = 5,

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    description = models.TextField(max_length=1500, blank=True)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    logo = models.ImageField(upload_to='station/logos/%Y/%m/%d/',
                             blank=True, null=True)

    rating = models.FloatField(default=0, editable=False)

    address = models.CharField(max_length=200)

    latitude = models.FloatField()
    longitude = models.FloatField()

    video = models.FileField(upload_to='stations/videos/%Y/%m/%d/', blank=True)
    comforts_array = ArrayField(
        models.IntegerField(choices=Comforts.choices),
        blank=True,
    )

    def __str__(self):
        return self.name


class StationImage(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to='stations/media/%Y/%m/%d/')
    ordering_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.ordering_number}'


class StationWorkTime(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='work_time')
    week_day = models.PositiveSmallIntegerField(choices=WeekDayChoices.choices)

    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = (('station', 'week_day'),)

    def __str__(self):
        return f'{self.start_time} - {self.end_time}'


class StationPetrolMark(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='petrol_mark')
    petrol_mark = models.PositiveSmallIntegerField(choices=PetrolMarkChoices.choices)

    number_of_columns = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=1)
    is_active = models.BooleanField(default=True)

    fill_time = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)], help_text='In seconds')

    def __str__(self):
        return f'{self.petrol_mark} Active: {self.is_active}'

    class Meta:
        unique_together = (('station', 'petrol_mark'),)


class StationRating(models.Model):
    station = models.ForeignKey(to=Station, on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0,
                                 validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('station', 'user'),)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.station.rating = StationRating.objects.aggregate(r=models.Avg('rating'))['r']
        self.station.save()