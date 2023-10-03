from django.urls import path

from kitchen.views import homepage, DishListView, DishTypeListView

urlpatterns = [
    path("", homepage, name="homepage"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
]

app_name = "kitchen"
