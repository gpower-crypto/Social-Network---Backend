from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserProfileSerializer
from .models import UserProfile

# Import necessary modules and classes

# Create your views here.

# Define a viewset for User-related operations

# I wrote this code

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    # Custom action for user registration
    @action(detail=False, methods=['POST'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom action to retrieve a user's friends
    @action(detail=False, methods=['GET'])
    def friends(self, request):
        user = request.user
        friends = user.userprofile.get_friends()
        serializer = UserSerializer(friends, many=True)
        return Response(serializer.data)

    # Custom action to create a user profile
    @action(detail=False, methods=['POST'])
    def create_profile(self, request):
        user = request.user
        profile_data = request.data

        # Create the UserProfile instance and associate it with the user
        profile_serializer = UserProfileSerializer(
            data=profile_data, context={'user': request.user})
        if profile_serializer.is_valid():
            profile = profile_serializer.save(user=user)
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom action to edit a user's profile
    @action(detail=True, methods=['PUT'])
    def edit_profile(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            profile = user.userprofile

            # Update the profile data with the new data from the request
            profile_data = request.data
            profile_serializer = UserProfileSerializer(
                instance=profile, data=profile_data, partial=True)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return Response(profile_serializer.data, status=status.HTTP_200_OK)
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Custom action to retrieve a user's profile
    @action(detail=True, methods=['GET'])
    def get_profile(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            profile = user.userprofile
            serializer = UserProfileSerializer(profile)

            # Include the username from the User model
            username = user.username
            profile_data = serializer.data
            profile_data['username'] = username

            return Response(profile_data)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Custom action to retrieve a user's status
    @action(detail=False, methods=['GET'])
    def status(self, request):
        # Get the current user's status
        user_profile = UserProfile.objects.get(user=request.user)
        status = user_profile.status
        return Response({'status': status})

    # Custom action to update a user's status
    @action(detail=False, methods=['PUT'])
    def update_status(self, request):
        # Get the current user's status
        user_profile = UserProfile.objects.get(user=request.user)

        # Update the user's status
        new_status = request.data.get('status', '')
        user_profile.status = new_status
        user_profile.save()

        return Response({'message': 'User status updated successfully'})

# end of code I wrote  