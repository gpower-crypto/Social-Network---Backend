from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import FriendRequest, User
from .serializers import FriendRequestSerializer
from rest_framework.decorators import action

# I wrote this code

class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def perform_create(self, serializer):
        # Set the 'from_user' when creating a friend request
        serializer.save(from_user=self.request.user)

    @action(detail=False, methods=['post'])
    def send_request(self, request):
        # Send a friend request
        to_user_id = request.data.get('to_user')
        from_user = request.user

        try:
            to_user = User.objects.get(id=to_user_id)
        except User.DoesNotExist:
            return Response({'detail': 'To user does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

        if to_user == from_user:
            return Response({'detail': 'You cannot send a friend request to yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        existing_request = FriendRequest.objects.filter(
            from_user=from_user, to_user=to_user).first()
        if existing_request:
            return Response({'detail': 'Friend request already sent.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FriendRequestSerializer(
            data={'from_user': from_user.id, 'to_user': to_user.id, 'status': 'pending'})
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Friend request sent.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'])
    def friend_requests(self, request):
        # Get friend requests for the current user
        user = self.request.user
        sent_requests = FriendRequest.objects.filter(from_user=user)
        received_requests = FriendRequest.objects.filter(to_user=user)

        serializer = FriendRequestSerializer(
            sent_requests.union(received_requests), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def accept_request(self, request, pk=None):
        # Accept a friend request
        friend_request = self.get_object()
        if friend_request.to_user == request.user and friend_request.status == 'pending':
            friend_request.status = 'accepted'
            friend_request.save()

            from_user = friend_request.from_user
            to_user = friend_request.to_user

            response_data = {
                'detail': 'Friend request accepted.',
                'from_user': from_user.username,
                'to_user': to_user.username
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response({'detail': 'Friend request not found or already accepted.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def reject_request(self, request, pk=None):
        # Reject a friend request
        friend_request = self.get_object()
        if friend_request.to_user == request.user and friend_request.status == 'pending':
            friend_request.status = 'rejected'
            friend_request.save()

            from_user = friend_request.from_user
            to_user = friend_request.to_user

            response_data = {
                'detail': 'Friend request rejected.',
                'from_user': from_user.username,
                'to_user': to_user.username
            }
            return Response(response_data, status=status.HTTP_200_OK)
        return Response({'detail': 'Friend request not found or already responded to.'}, status=status.HTTP_400_BAD_REQUEST)

# end of code I wrote  