from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new_user/', views.new_user, name="new_user"),
    path('logged_in_user/', views.logged_in_user, name="logged_in_user"),
]