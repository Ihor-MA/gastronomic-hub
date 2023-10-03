from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from kitchen.models import Dish, DishType, Cook


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "dish_type", "price"]
    search_fields = ("name",)
    list_filter = ("dish_type", )


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "years_of_experience", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("years_of_experience",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "years_of_experience",
                )
            }
        ),
    )


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ("name", )

