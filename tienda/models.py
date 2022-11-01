from django.db import models
class Marca(models.Model):
    nombre = models.CharField(max_length=30)

class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidades = models.IntegerField()
    precio = models.IntegerField()
    detalles = models.CharField(max_length=30)

class Compra(models.Model):
    fecha = models.DateField()
    unidades = models.IntegerField()
    importe = models.CharField(max_length=30)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)



