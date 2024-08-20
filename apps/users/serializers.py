from django.contrib.auth import get_user_model
from rest_framework import serializers



class CustomUserSerializer(serializers.ModelSerializer):
    region = serializers.CharField(source='get_region_display', read_only=True)
    district = serializers.CharField(source='get_district_display', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'phone_number', 'balance', 'email', 'region', 'district']
        extra_kwargs = {
            'phone_number': {'read_only': True},
            'balance': {'read_only': True},
            'region': {'write_only': True},
            'district': {'write_only': True},
        }

    def validate(self, attrs):
        attrs = super().validate(attrs)
        model = get_user_model()(**attrs)
        model.clean()
        return attrs