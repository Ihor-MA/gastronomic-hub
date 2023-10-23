from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType, Cook

DISH_LIST_URL = reverse("kitchen:dish-list")
DISH_TYPE_LIST_URL = reverse("kitchen:dish-type-list")
COOK_LIST_URL = reverse("kitchen:cook-list")


class PublicDishTest(TestCase):
    def test_login_required_list(self):
        res = self.client.get(DISH_LIST_URL)
        self.assertNotEquals(res.status_code, 200)

    def test_login_required_detail(self):
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

        detail_url = reverse("kitchen:dish-detail", kwargs={"pk": dish.pk})
        res = self.client.get(detail_url)
        self.assertNotEquals(res.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123",
        )
        self.client.force_login(self.user)

    def test_retrieve_manufacturers(self):
        dish_type = DishType.objects.create(
            name="soup"
        )
        dish_type2 = DishType.objects.create(
            name="misosoup"
        )
        Dish.objects.create(
            name="Soup1",
            description=("Crisp romaine lettuce, croutons, and Parmesan"
                         " cheese tossed in Caesar dressing."),
            price=5.99,
            dish_type=dish_type,
        )
        Dish.objects.create(
            name="Soup2",
            description=("Great soup.", ),
            price=8.99,
            dish_type=dish_type2,
        )
        response = self.client.get(DISH_LIST_URL)
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes),
        )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")


class PublicDishTypeTest(TestCase):
    def test_login_required_list(self):
        res = self.client.get(DISH_TYPE_LIST_URL)
        self.assertNotEquals(res.status_code, 200)

    def test_login_required_detail(self):
        dish_type = DishType.objects.create(
            name="soup"
        )

        detail_url = reverse(
            "kitchen:dish-type-detail",
            kwargs={"pk": dish_type.pk}
        )
        res = self.client.get(detail_url)
        self.assertNotEquals(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123",
        )
        self.client.force_login(self.user)

    def test_retrieve_manufacturers(self):
        DishType.objects.create(
            name="soup"
        )
        DishType.objects.create(
            name="misosoup"
        )

        response = self.client.get(DISH_TYPE_LIST_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types),
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")


class PublicCookTest(TestCase):
    def test_login_required_list(self):
        res = self.client.get(COOK_LIST_URL)
        self.assertNotEquals(res.status_code, 200)

    def test_login_required_detail(self):
        cook = get_user_model().objects.create(
            username="leo.messi",
            password="leomessipassword",
            first_name="Lionel",
            last_name="Messi",
        )
        detail_url = reverse("kitchen:cook-detail", kwargs={"pk": cook.pk})
        res = self.client.get(detail_url)
        self.assertNotEquals(res.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123",
        )
        self.client.force_login(self.user)

    def test_retrieve_manufacturers(self):
        get_user_model().objects.create(
            username="leo.messi",
            password="leomessipassword",
            first_name="Lionel",
            last_name="Messi",
            years_of_experience=5,
        )
        get_user_model().objects.create(
            username="frenkie22",
            password="fren22",
            first_name="Frenkie",
            last_name="De Jong",
        )

        response = self.client.get(COOK_LIST_URL)
        self.assertEqual(response.status_code, 200)
        cooks = Cook.objects.all()
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks),
        )
        self.assertTemplateUsed(response, "kitchen/cook_list.html")
