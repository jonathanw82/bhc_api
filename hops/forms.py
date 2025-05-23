# In your forms.py
from django import forms
from .models import Hops_species, Plant_weight, User_plant


class Hops_species_form(forms.ModelForm):
    class Meta:
        model = Hops_species
        fields = ['name', 'description', 'origin', 'primary_use',
                  'height', 'also_known_as', 'beer_style_guide',
                  'flavour']


class User_plant_form(forms.ModelForm):
    class Meta:
        model = User_plant
        fields = ['species', 'date_planted']


class Plant_weight_form(forms.ModelForm):
    class Meta:
        model = Plant_weight
        fields = ['species', 'weight_kg']
