from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import InnoFoodUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    class Meta:
        model = InnoFoodUser
        fields = ["username", "email", "password"]

