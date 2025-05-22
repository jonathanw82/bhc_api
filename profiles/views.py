from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import User_Profile


@login_required
def profile(request):
    """ A view to display the Users personal details """
    user = request.user
    first_name = User_Profile.objects.filter(first_name=user)
    last_name = User_Profile.objects.filter(last_name=user)
    phone = User_Profile.objects.filter(phone_number=user)
    membership_num = User_Profile.objects.filter(membership_number=user)

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'membership_number': membership_num,
    }
    return render(request, 'apiary/apiary.html', context)