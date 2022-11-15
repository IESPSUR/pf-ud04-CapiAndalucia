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

class CantidadCompra(forms.Form):
    unit = forms.IntegerField(label='unit')

    def clean_minas(self):
        unit = self.cleaned_data.get('unit')
        if unit is None:
            raise ValidationError("TE PASASTE!")
        return unit



