from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, get_jwt_token, api_auth_key

v1_router = routers.DefaultRouter()
v1_router.register('users', UserViewSet)

urlpatterns = [
    path('v1/auth/email/', api_auth_key),
    path('v1/auth/token/', get_jwt_token),
    path('v1/', include(v1_router.urls)),
]
