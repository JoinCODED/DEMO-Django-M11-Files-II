from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ships import models
from ships.forms import ShipForm


def get_ships(request: HttpRequest) -> HttpResponse:
    ships: list[models.Ship] = list(models.Ship.objects.all())

    context = {
        "ships": ships,
    }

    return render(request, "ship_list.html", context)


def create_ship(request: HttpRequest) -> HttpResponse:
    form = ShipForm()
    context = {
        "form": form,
    }
    return render(request, "create_ship.html", context)
