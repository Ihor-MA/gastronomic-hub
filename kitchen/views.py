from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import DishForm, CookCreationForm, CookUpdateForm
from .models import Dish, DishType, Cook


@login_required
def homepage(request):
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dishes": Dish.objects.count(),
        "num_dish_types": DishType.objects.count(),
        "num_cooks": Cook.objects.count(),
        "num_visits": num_visits + 1,
    }

    return render(request, "kitchen/homepage.html", context=context)


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 5


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "kitchen/dish_type_detail.html"
    context_object_name = "dish_type"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = ("name", )
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen:cook-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = ("name", )
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    success_url = reverse_lazy("kitchen:cook-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
