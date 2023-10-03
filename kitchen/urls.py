from django.urls import path

from kitchen.views import homepage, DishListView

urlpatterns = [
    path("", homepage, name="homepage"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
]

app_name = "kitchen"
