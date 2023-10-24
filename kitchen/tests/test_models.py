from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="soup"
        )
        self.assertEqual(
            str(dish_type),
            dish_type.name
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="soup"
        )
        dish = Dish.objects.create(
            name="Salad",
            description=("Crisp romaine lettuce, croutons, and Parmesan"
                         " cheese tossed in Caesar dressing."),
            price=5.99,
            dish_type=dish_type,
        )
        self.assertEqual(
            str(dish),
            dish.name
        )

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="leo.messi",
            password="leomessipassword",
            first_name="Lionel",
            last_name="Messi",
            years_of_experience=5,
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )
