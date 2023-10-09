from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# I wrote this code

router = DefaultRouter()
# Register the PostViewSet with the router
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = router.urls

# end of code I wrote  