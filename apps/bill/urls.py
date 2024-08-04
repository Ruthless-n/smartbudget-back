from django.urls import path
from . import views


urlpatterns = [
    path('bills/', views.list_bills, name="list-bills"),
    path('bills/<int:id_bill>', views.detail_bills, name="detail-bills"),
    path('bills/user/<int:responsible>', views.list_bills_by_user, name="list-bills-by-user")
]
