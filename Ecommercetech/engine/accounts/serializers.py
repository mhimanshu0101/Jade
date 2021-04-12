from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=256)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=256, read_only=True)
    name = serializers.CharField(read_only=True)
    user_type = serializers.IntegerField(read_only=True)
    code = serializers.CharField(read_only=True)
    registration_date = serializers.DateField(read_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email is None:
            raise serializers.ValidationError(
                'Email field is required to login'
            )
        if password is None:
            raise serializers.ValidationError(
                'Password is required to login.'
            )
        
        # The `authenticate` method provided by Django, handles checking for a user
        # that matches this email and password combination.
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.validationError(
                'A user with this email and password not found.'
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                'User is not active'
            )
        
        return {
            'email': user.email,
            'token': user.token,
            'user_type': user.user_type,
            'name': user.name,
            'code': user.code,
            'registration_date': user.registration_date
        }
