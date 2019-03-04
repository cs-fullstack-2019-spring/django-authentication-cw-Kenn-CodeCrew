from django.shortcuts import render
from django.http import HttpResponse
from .forms import FoodFitnessForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, "AuthenticationApp/index.html")


def new_user(request):
    form = FoodFitnessForm()
    context = {"form": form}
    return render(request, "AuthenticationApp/new_user.html", context)


def logged_in_user(request):
    User.objects.create_user(request.POST["username"], '', '')
    return render(request, "AuthenticationApp/logged_in_user.html")
