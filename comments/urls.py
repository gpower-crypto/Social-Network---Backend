from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

# I wrote this code

# DefaultRouter for managing API endpoints.
router = DefaultRouter()
# Register the CommentViewSet with the router.
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = router.urls

# end of code I wrote  