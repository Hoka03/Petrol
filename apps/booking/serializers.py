from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from urllib3 import request

from .models import Booking


class BookingCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_car(self, car):
        user = self.context['request'].user
        if not user.usercar_set.filter(id=car.id).exists():
            raise ValidationError('Car not found')

    class Meta:
        model = Booking
        fields = ('station_petrol_mark', 'car', 'user', 'quantity', 'booking_time')