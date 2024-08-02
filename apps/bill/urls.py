from django.urls import path
from . import views


urlpatterns = [
    path('bills/', views.list_bills, name="list-bills"),
    path('bills/<int:id_bill>', views.detail_bills, name="detail-bills")
]
