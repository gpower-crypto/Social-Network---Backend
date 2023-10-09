from rest_framework import serializers
from .models import Comment

# I wrote this code

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    
# end of code I wrote  