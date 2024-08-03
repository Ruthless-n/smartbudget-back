from rest_framework.decorators import api_view, permission_classes
from django.urls import path, include
from .serializers import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('user/', views.create_user, name='create-user'),
    path('user/<int:id_user>', views.detail_user, name='detail-user'),
    path('user/auth/', CustomTokenObtainPairView.as_view(), name='user_auth'),
    path('user/refresh/', TokenRefreshView.as_view(), name='user_auth_refresh'),
]