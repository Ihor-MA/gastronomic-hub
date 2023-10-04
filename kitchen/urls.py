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
    DishUpdateView,
    DishTypeUpdateView,
    CookUpdateView,
    DishDeleteView,
    DishTypeDeleteView,
    CookDeleteView,
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
    path("dishes/update/<int:pk>/", DishUpdateView.as_view(), name="dish-update"),
    path("dish-types/update/<int:pk>/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("cooks/update/<int:pk>/", CookUpdateView.as_view(), name="cook-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dish-types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),

]

app_name = "kitchen"
