from django.test import TestCase

from kitchen.forms import DishSearchForm, DishTypeSearchForm, CookSearchForm


class DishSearchFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            "name": "TestDish",
        }
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_empty_data(self):
        form_data = {}
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_widget_attrs(self):
        form = DishSearchForm()
        name_widget = form.fields["name"].widget
        self.assertIn("placeholder", name_widget.attrs)
        self.assertEqual(name_widget.attrs["placeholder"], "Search by name")


class DishTypeSearchFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            "name": "TestDishType",
        }
        form = DishTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_empty_data(self):
        form_data = {}
        form = DishTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_widget_attrs(self):
        form = DishTypeSearchForm()
        name_widget = form.fields["name"].widget
        self.assertIn("placeholder", name_widget.attrs)
        self.assertEqual(name_widget.attrs["placeholder"], "Search by name")


class CookSearchFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            "name": "TestDishType",
        }
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_empty_data(self):
        form_data = {}
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_widget_attrs(self):
        form = CookSearchForm()
        name_widget = form.fields["username"].widget
        self.assertIn("placeholder", name_widget.attrs)
        self.assertEqual(
            name_widget.attrs["placeholder"],
            "Search by username"
        )
