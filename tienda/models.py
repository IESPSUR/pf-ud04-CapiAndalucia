from django.db import models
class Marca(models.Model):
    nombre = models.CharField('Nombre', max_length=30, unique=True)

class Productos(models.Model):
    nombre = models.CharField('Nombre',max_length=30)
    modelo = models.CharField('Modelo', max_length=30)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidades = models.IntegerField('Unidades')
    precio = models.DecimalField('Precio', max_digits=5, decimal_places=2, default=0)
    detalles = models.CharField('Detalles',max_length=30, null=True)

class Compra(models.Model):
    fecha = models.DateField('Fecha')
    unidades = models.IntegerField('Unidades')
    importe = models.CharField('Importe',max_length=30)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)



