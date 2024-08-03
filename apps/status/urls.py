from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.status_list, name='status-list'),
]