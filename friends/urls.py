from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FriendRequestViewSet

# I wrote this code

router = DefaultRouter()
router.register(r'friend-requests', FriendRequestViewSet,
                basename='friend-requests')

urlpatterns = router.urls

# end of code I wrote  