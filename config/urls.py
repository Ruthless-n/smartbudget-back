from django.urls import (
    include,
    path,
)

from django.contrib import admin

urlpatterns = [
    path('admin/e79b4008-b2b6-4e78-8dca-1696b92df35a/', admin.site.urls),
    path("", include("apps.core.urls")),
    path('api/v1/', include('apps.user.urls')),
    path('api/v1/', include('apps.bill.urls')),
    path('api/v1/', include('apps.category.urls'))
]
