from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

# Serializer for the UserProfile model

# I wrote this code

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'bio', 'location', 'profile_picture']

# Serializer for the User model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # 'password' field is write-only
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

# end of code I wrote  