from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileSetupView

# I wrote this code

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = router.urls

# end of code I wrote  