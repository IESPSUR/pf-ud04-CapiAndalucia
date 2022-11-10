from django.core.exceptions import ValidationError

def validar_Textos(value):
    texto = len(value)
    if texto > 30:
        raise ValidationError('Sobrepasó los 30 caracteres')
    return value

