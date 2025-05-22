from django import forms
from .models import User_Profile


class User_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['first_name', 'last_name', 'phone_number', 'join_year']