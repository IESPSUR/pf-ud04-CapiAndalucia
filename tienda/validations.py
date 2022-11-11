from django.core.exceptions import ValidationError
import re

def validar_Textos(value):
    texto = len(value)
    if texto > 30:
        raise ValidationError('Sobrepasó los 30 caracteres')
    return value

def validar_precio(value):
    numero = str(value)
    patron = re.compile('^[0-9]{0,5}(.){0,1}[0-9]{0,2}$')

    if not patron.search(numero):
        raise ValidationError('Sobrepasa el limite')

    return value

