from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Dish, DishType, Cook


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
