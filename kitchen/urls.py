from django.urls import path

from kitchen.views import (
    homepage,
    DishListView,
    DishTypeListView,
    CookListView,
    DishDetailView,
    CookDetailView,
    DishTypeDetailView,
    DishCreateView,
    DishTypeCreateView,
    CookCreateView,
)

urlpatterns = [
    path("", homepage, name="homepage"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("dish-types/<int:pk>/", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),

]

app_name = "kitchen"
