from django.urls import path

from kitchen.views import homepage

urlpatterns = [
    path("", homepage, name="homepage"),
]

app_name = "kitchen"
