from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FoodFitnessModel(models.Model):
    username = models.CharField(max_length=200)
    calories = models.DecimalField(decimal_places=2, max_digits=7)
    date = models.DateField(default="")
    linkToForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "Username is: " + self.username
