from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Comment, User
from .serializers import CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from posts.models import Post

# I wrote this code

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['GET'])
    def get_comments(self, request):
        # Get comments for a specific user and post
        user_id = request.query_params.get('user_id')
        post_id = request.query_params.get('post_id')

        try:
            post = Post.objects.get(pk=post_id)
            comments = Comment.objects.filter(post=post, user=user_id)
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['POST'])
    def create_comment(self, request):
        # Create a new comment
        user_id = request.query_params.get('user_id')
        post_id = request.query_params.get('post_id')

        try:
            post = Post.objects.get(pk=post_id)
            user = User.objects.get(pk=user_id)
            comment_data = {
                'user': user.pk,
                'post': post.pk,
                'text': request.data.get('text')
            }
            comment_serializer = CommentSerializer(data=comment_data)
            if comment_serializer.is_valid():
                comment_serializer.save()
                return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except (Post.DoesNotExist, User.DoesNotExist):
            return Response({'detail': 'Post or User not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['PUT', 'DELETE'])
    def edit_comment(self, request):
        # Edit or delete a comment
        user_id = request.query_params.get('user_id')
        comment_id = request.query_params.get('comment_id')

        try:
            user = User.objects.get(pk=user_id)
            comment = Comment.objects.get(pk=comment_id, user=user)

            if request.method == 'PUT':
                comment_text = request.data.get('text')
                comment.text = comment_text
                comment.save()

                serializer = CommentSerializer(comment)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif request.method == 'DELETE':
                comment.delete()
                return Response({'detail': 'Comment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except (User.DoesNotExist, Comment.DoesNotExist):
            return Response({'detail': 'User or Comment not found.'}, status=status.HTTP_404_NOT_FOUND)

# end of code I wrote  