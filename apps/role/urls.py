from django.urls import path
from . import views


urlpatterns = [
    path('role/', views.list_category , name='list-category'),
]
