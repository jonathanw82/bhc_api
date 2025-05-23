from django.db import models
from django.contrib.auth.models import User


class Hops_species(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    origin = models.CharField(max_length=50, unique=True)
    primary_use = models.CharField(max_length=100, unique=True)
    height = models.CharField(max_length=20)
    also_known_as = models.CharField(max_length=100)
    beer_style_guide = models.CharField(max_length=100)
    flavour = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User_plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='plants')
    species = models.ForeignKey(Hops_species, on_delete=models.SET_NULL,
                                null=True, blank=True)
    date_planted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.species.name if self.species else
                               'Unknown Species'}) by {self.user.username}"


class Plant_weight(models.Model):
    species = models.ForeignKey(User_plant, on_delete=models.CASCADE,
                              related_name='weight_entries')
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2)  # Adjust max_digits and decimal_places as needed
    timestamp = models.DateTimeField(auto_now_add=True)  # Records when the weight was added

    def __str__(self):
        return f"{self.plant.name} - {self.weight}g on\
              {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
