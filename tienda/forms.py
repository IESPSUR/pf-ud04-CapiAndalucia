from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Productos


class ProductosForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass


