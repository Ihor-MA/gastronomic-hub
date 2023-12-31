from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("kitchen.urls", namespace="kitchen")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
