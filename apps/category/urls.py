from django.urls import path
from . import views


urlpatterns = [
    path('category/', views.list_category , name='list-category'),
    path('category/<int:id_category>', views.detail_category, name='detail-category')
]
