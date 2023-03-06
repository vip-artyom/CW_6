from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import CustomUser

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name',
                  'last_name',
                  'email',
                  'password',
                  'phone',
                  'image']


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name',
                  'last_name',
                  'email',
                  'phone',
                  'id',
                  'image']
