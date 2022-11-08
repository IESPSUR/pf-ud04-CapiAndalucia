from django.shortcuts import render
from tienda.models import Productos


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html', {})


def listado_producto(request):

    posts = Productos.objects.all()

    return render(request, 'tienda/listado.html', {'posts': posts})

def edicion(request):

    return render(request, 'tienda/edicion.html', {})
