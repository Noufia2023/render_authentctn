from django.urls import path, include
from rest_framework import routers
from .views import SignUpViewSet

router = routers.DefaultRouter()
router.register(r'signup', SignUpViewSet, basename='signup'),


urlpatterns = [
    path('', include(router.urls)),
    # Define other URLs for login, logout, etc.
]
