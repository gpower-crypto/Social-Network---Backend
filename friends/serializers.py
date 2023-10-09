from rest_framework import serializers
from .models import FriendRequest

# I wrote this code

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'

    def create(self, validated_data):
        return FriendRequest.objects.create(**validated_data)
    

# end of code I wrote  