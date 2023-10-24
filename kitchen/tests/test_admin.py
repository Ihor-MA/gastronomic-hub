from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin123",
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="cook123",
        )

    def test_cook_detail_years_of_experience_listed(self):
        """
        Test that cook`s years_of_experience
        is in list_display on cook detail admin page
        """
        url = reverse("admin:kitchen_cook_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_years_of_experience_listed(self):
        """
        Test that cook`s years_of_experience is in list_display
        on cook admin page
        """
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        res = self.client.get(url)
        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_years_of_experience_in_add_fieldsets(self):
        """
        Test that cook`s years_of_experience is in add_fieldsets
         on cook admin page
        """
        url = reverse("admin:kitchen_cook_add")
        res = self.client.get(url)

        self.assertContains(
            res,
            '<input type="number" name="years_of_experience"'
        )
