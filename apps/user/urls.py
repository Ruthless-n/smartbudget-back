from django.contrib import admin
from django.urls import path, include
from .serializers import CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views



