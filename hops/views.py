from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User_plant, Plant_weight
from .forms import Plant_weight_form 


@login_required
def add_plant_weight(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id, user=request.user)

    if request.method == 'POST':
        form = Plant_weight_form(request.POST)
        if form.is_valid():
            weight_entry = form.save(commit=False)
            weight_entry.plant = plant
            weight_entry.save()
            return redirect('plant_detail', plant_id=plant.id) # Redirect to the plant's detail page
    else:
        form = Plant_weight_form()

    return render(request, 'add_weight.html', {'form': form, 'plant': plant})


@login_required
def add_plant_weight(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id, user=request.user)

    if request.method == 'POST':
        form = Plant_weight_form(request.POST)
        if form.is_valid():
            weight_entry = form.save(commit=False)
            weight_entry.plant = plant
            weight_entry.save()
            return redirect('plant_detail', plant_id=plant.id) # Redirect to the plant's detail page
    else:
        form = Plant_weight_form()

    return render(request, 'add_weight.html', {'form': form, 'plant': plant})
