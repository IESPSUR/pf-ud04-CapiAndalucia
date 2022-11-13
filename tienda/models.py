from django.db import models
from .validations import validar_Textos, validar_precio

class Marca(models.Model):
    nombre = models.CharField('Nombre',  max_length=50, validators=[validar_Textos], unique=True, primary_key=True)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField('Nombre',max_length=50, validators=[validar_Textos])
    modelo = models.CharField('Modelo', max_length=50,validators=[validar_Textos])
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    unidades = models.IntegerField('Unidades')
    precio = models.FloatField('Precio', validators=[validar_precio], default=0)
    detalles = models.CharField('Detalles',max_length=50,validators=[validar_Textos], null=True)

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    fecha = models.DateField('Fecha')
    unidades = models.IntegerField('Unidades')
    importe = models.CharField('Importe',max_length=50,validators=[validar_Textos])
    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True)
    nombre_usuario = models.CharField('Nombre Usuario',max_length=50)






