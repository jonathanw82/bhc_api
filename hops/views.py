from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Hops_species, Plants_assigned_to_user, Plant_weight
from .forms import Plant_weight_form, User_plant_form, Hops_species_form


@login_required
def add_hop_varieties(request):
    """ A view to alow admins to add hops varieties """

    if request.method == 'POST':
        form = Hops_species_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_plants_admin')
    else:
        form = Hops_species_form()
    context = {
        'form': form,
    }

    return render(request, 'hops/add_plant.html', context)



@login_required
def add_plant_to_user(request):
    """ A view to allow user to select their personal variety """

    plant = Hops_species.objects.all()

    if request.method == 'POST':
        form = User_plant_form(request.POST)
        if form.is_valid():
            new_plant = form.save(commit=False)
            new_plant.plant = plant
            new_plant.save()
            return redirect('plant_detail')
    else:
        form = User_plant_form()
    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'hops/add_plant.html', context)


@login_required
def user_update_plant(request, plant_id):
    """ A view to updating a plant by user """

    plant = get_object_or_404(User_plant, pk=plant_id)
    if request.method == 'POST':
        form = User_plant_form(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('all_products_admin')
    else:
        form = User_plant_form(instance=plant)
    context = {
        'form': form,
        'plant_id': plant_id,
    }
    return render(request, 'hops/update_plant.html', context)


@login_required
def user_plant_view(request):
    """A view for user to see their plants and weights"""

    plant = User_plant.objects.filter(user=request.user)
    weight = Plant_weight.objects.filter(plant.id, user=request.user)
    context = {
        "plant": plant,
        "weight": weight
    }

    return render(request, 'hops/user_plants.html', context)


@login_required
def add_plant_weight(request, plant_id):
    """A view so users can add plant weights to a specific plant """

    plant = get_object_or_404(User_plant, id=plant_id, user=request.user)

    if request.method == 'POST':
        form = Plant_weight_form(request.POST)
        if form.is_valid():
            weight_entry = form.save(commit=False)
            weight_entry.plant = plant
            weight_entry.save()
            return redirect('plant_detail', plant_id=plant.id)
    else:
        form = Plant_weight_form()
    context = {
        'form': form,
        'plant': plant,
    }

    return render(request, 'hops/add_weight.html', context)


@login_required
def view_plant_data(request, plant_id):
    """ A view to a plants data """
    plant = get_object_or_404(Hops_species, id=plant_id)
    context = {
        "plant": plant,
    }
    return render(request, 'view_plant_data.html', context)


@login_required
def all_plants_admin(request):
    """ A view for admins to all plants admin """

    all_plants = Hops_species.objects.all()

    context = {
        'all_plants': all_plants,
    }
    return render(request, 'all_plants_admin.html', context)


@login_required
def admin_update_plant_data(request, plant_id):
    """ A view to updating a plant """

    plant = get_object_or_404(Hops_species, id=plant_id)
    if request.method == 'POST':
        form = Hops_species_form(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('view_plant_data', plant_id=plant_id)
    else:
        form = Hops_species_form(instance=plant)
    context = {
        'form': form,
        'plant_id': plant_id,
    }
    return render(request, 'update_plant.html', context)


@login_required
def delete(request, plant_id):
    """ A view to delete hops varieties in admin """

    plant = get_object_or_404(Hops_species, id=plant_id)
    plant.delete()
    return redirect(reverse('all_plants_admin'))
