from django import forms
from django.core.exceptions import ValidationError

from .models import Productos


class ProductosForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = '__all__'




