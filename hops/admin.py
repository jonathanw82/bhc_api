from django.contrib import admin
from .models import Hops_species, Plants_assigned_to_user, Plant_weight, Tasting_notes

# Register your models here.
admin.site.register(Hops_species)
admin.site.register(Plants_assigned_to_user)
admin.site.register(Plant_weight)
admin.site.register(Tasting_notes)
