from django.urls import path
from . import views

urlpatterns = [
    path('add_hop_varieties/', views.add_hop_varieties,
         name='add_hop_varieties'),
    path('add_plant_to_user/', views.add_plant_to_user,
         name='add_plant_to_user'),
    path('user_plant_view/', views.user_plant_view, name='user_plant_view'),
    path('user_update_plant/<plant_id>', views.user_update_plant,
         name='user_update_plant'),
    path('add_plant_weight/', views.add_plant_weight, name='add_plant_weight'),
    path('all_plants_admin/', views.all_plants_admin, name='all_plants_admin'),
    path('admin_update_plant_variety/<plant_id>', 
         views.admin_update_plant_variety, name='admin_update_plant_variety'),
    path('delete/<plant_id>', views.delete, name='delete'),
]
