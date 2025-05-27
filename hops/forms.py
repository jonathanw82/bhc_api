# In your forms.py
from django import forms
from .models import Hops_species, Plant_weight, Plants_assigned_to_user


class Hops_species_form(forms.ModelForm):
    class Meta:
        model = Hops_species
        fields = ['name', 'description', 'origin', 'primary_use',
                  'height', 'also_known_as', 'beer_style_guide',
                  'flavor']


class User_plant_form(forms.ModelForm):
    class Meta:
        model = Plants_assigned_to_user
        fields = ['species', 'date_planted']
        widgets = {
            'date_planted': forms.DateInput(attrs={'type': 'date'}),
        }


class Plant_weight_form(forms.ModelForm):
    class Meta:
        model = Plant_weight
        fields = ['species', 'weight_kg']
