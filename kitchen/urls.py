from django.urls import path

from kitchen.views import (
    homepage,
    DishListView,
    DishTypeListView,
    CookListView,
    DishDetailView,
    CookDetailView,
)

urlpatterns = [
    path("", homepage, name="homepage"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
]

app_name = "kitchen"
