from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Productos

"""
Form que utiliza los valores exactos del modelo Productos 
"""
class ProductosForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass

class CanidadCompra(forms.Form):
    unit = forms.IntegerField(label='unit', max_value=100, min_value=1)


