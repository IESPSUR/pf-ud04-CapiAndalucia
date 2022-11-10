from django.shortcuts import render, redirect
from tienda.models import Productos, Marca
from .forms import ProductosForm

from django.contrib.auth.models import User


# Create your views here.
def welcome(request):
    
    return render(request, 'tienda/index.html', {})


def listado_producto(request):

    posts = Productos.objects.all()
    elementos = []
    elementos.append(posts)
    #formulario = ProductosForm(request.POST)
    return render(request, 'tienda/listado.html', {'posts': posts, 'elemetos':elementos})

#Creamos un metodo el cual modifica el producto que nos pasan como parametro
def editar(request, pk):
    produc = Productos.objects.get(id = pk)
    posts = Productos.objects.all()
    marca = Marca.objects.all()


    formulario = ProductosForm(request.POST or None, instance=produc)

    if request.method == 'POST' and formulario.is_valid():

        formulario.save()
        return render(request, 'tienda/listado.html', {'posts': posts})

    return render(request, 'tienda/edicion.html', {'formulario' : formulario, 'produc':produc, 'posts':marca})

#Creamos un metrodo el cual recibe el request y el id del producto que queremos eliminar
def eliminar(request, pk):
    #devolvemos el producto a traves del id que le hemos pasado
    produc = Productos.objects.get(id=pk)
    posts = Productos.objects.all()
    produc.delete()
    return render(request, 'tienda/listado.html', {'posts': posts})

def actualizado(request):
    return render()
