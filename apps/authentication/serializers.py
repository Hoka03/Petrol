import random

from django.contrib.gis.measure import pretty_name
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import serializers

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.contrib.auth.password_validation import validate_password

from apps.users.validations import phone_validate


class SendAuthCodeSerializer(serializers.Serializer):  # first part
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate])
    code = serializers.IntegerField(read_only=True)

    @staticmethod
    def send_code(phone_number, code):
        print('sended')

    def check_limit(self):
        # checking limit for ip address
        request = self.context.get('request')
        ip_address = request.META.get('REMOTE_ADDR')

        limit = cache.get(ip_address, 0)
        if limit >= 3:
            raise ValidationError('try after one hour')
        else:
            cache.set(ip_address, limit + 1, 60 * 60)

    @staticmethod
    def generate_code():
        return random.randint(1000, 9999)

    def validate_phone_number(self, phone_number):
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('User have not create like this name')
        return phone_number

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number = attrs['phone_number']

        self.check_limit()

        attrs['code'] = self.generate_code()
        self.send_code(phone_number, attrs['code'])
        cache.set(f'{phone_number}_auth_code', attrs['code'], 10 * 60)

        return attrs


class VerifyCodeSerializer(serializers.Serializer):  # second part
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate], write_only=True)
    code = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)

        phone_number, code = attrs['phone_number'], attrs['code']

        if cache.get(f"{phone_number}_auth_code") != code:
            print(attrs['phone_number'])
            raise serializers.ValidationError("Code was entered mistake. Please try again.")

        return attrs


class RegisterSerializer(VerifyCodeSerializer):     # third part
    password = serializers.CharField(max_length=120, validators=[validate_password], write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)

        # if 'phone_number' or 'password' not in attrs:
        #     raise ValidationError("Phone number and password are required.")

        phone_number, password = attrs['phone_number'], attrs['password']

        user = get_user_model().objects.create_user(phone_number=phone_number, password=password)

        token = Token.objects.create(user_id=user.id)
        attrs['token'] = token.key

        cache.delete(f"{phone_number}_auth_code")

        return attrs


class LoginSerializer(serializers.Serializer):  # last part
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate])
    password = serializers.CharField(max_length=120, write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, password = attrs['phone_number'], attrs['password']

        user = get_object_or_404(get_user_model(), phone_number=phone_number)
        if not user.check_password(password):
            return ValidationError('Phone number or password was mistake.')

        token, _ = Token.objects.get_or_create(user_id=user.id)
        attrs['token'] = token.key

        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=13, validators=[phone_validate])
    password = serializers.CharField(max_length=120, write_only=True)
    code = serializers.IntegerField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number = attrs['phone_number']
        password = attrs['password']
        code = attrs['code']

        if cache.get(f"{phone_number}_auth_change_password") != code:
            raise ValidationError('Phone number or code was mistake.')

        user = get_object_or_404(get_user_model(), phone_number=attrs['phone_number'])

        user.set_password(password)
        user.save()

        token, _ = Token.objects.get_or_create(user_id=user.id)
        attrs['token'] = token.key

        cache.delete(f"{phone_number}_auth_change_password")

        return attrs

