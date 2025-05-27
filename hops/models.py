from django.db import models
from django.contrib.auth.models import User


class Tasting_notes(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Hops_species(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    origin = models.CharField(max_length=50, blank=True)
    primary_use = models.CharField(max_length=100, blank=True)
    height = models.CharField(max_length=20)
    also_known_as = models.CharField(max_length=100, blank=True)
    beer_style_guide = models.CharField(max_length=100, blank=True)
    flavor = models.ManyToManyField(Tasting_notes, related_name='hops_varieties', blank=True)

    def __str__(self):
        return self.name


class Plants_assigned_to_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='plants')
    species = models.ForeignKey(Hops_species, on_delete=models.SET_NULL,
                                null=True, blank=True)
    date_planted = models.DateField()

    def __str__(self):
        return f"{self.species}"


class Plant_weight(models.Model):
    species = models.ForeignKey(Plants_assigned_to_user, on_delete=models.CASCADE,
                                related_name='weight_entries')
    weight_kg = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.species} - {self.weight_kg}g on\
              {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
