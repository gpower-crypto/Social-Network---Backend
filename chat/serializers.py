from rest_framework import serializers
from .models import ChatMessage

# serializer class for the ChatMessage model.

# I wrote this code

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = "__all__"

# end of code I wrote  