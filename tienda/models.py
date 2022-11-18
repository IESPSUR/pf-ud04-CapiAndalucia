from django.contrib.auth.models import User
from django.db import models
from .validations import validar_Textos, validar_precio

class Marca(models.Model):
    """
    Almacena los nombres de las marcas que trabajan con la tienda
    """
    nombre = models.CharField('Nombre',  max_length=50, validators=[validar_Textos], unique=True, primary_key=True)

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    """
    Almacena los productos que se venden en la tienda
    """
    nombre = models.CharField('Nombre',max_length=50, validators=[validar_Textos])
    modelo = models.CharField('Modelo', max_length=50,validators=[validar_Textos])
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)
    unidades = models.IntegerField('Unidades') #PositiveIntegerField solo deja colocar numeros positivos
    precio = models.FloatField('Precio', validators=[validar_precio], default=0)
    detalles = models.TextField('Detalles',max_length=500, null=True)

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    """
    Almacena las compras que que se realice la tienda
    """
    fecha = models.DateField('Fecha')
    unidades = models.IntegerField('Unidades')
    importe = models.CharField('Importe',max_length=50,validators=[validar_Textos])
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    nombre_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' ' + str(self.producto)






