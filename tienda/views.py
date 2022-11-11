from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from tienda.models import Productos, Marca
from .forms import ProductosForm
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.models import User


# Create your views here.
def welcome(request):
    
    return render(request, 'tienda/index.html', {})

#@user_passes_test(lambda u: u.is_superuser)
def listado_producto(request):
    userform = UserCreationForm(request.POST)
    if request.user.is_superuser:
        posts = Productos.objects.all()
        elementos = []
        elementos.append(posts)
        #formulario = ProductosForm(request.POST)
        return render(request, 'tienda/listado.html', {'posts': posts, 'elemetos':elementos})
    else:
        return render(request, 'registration/registro.html', {"form": userform})

#Creamos un metodo el cual modifica el producto que nos pasan como parametro
#@user_passes_test(lambda u: u.is_superuser)
def editar(request, pk):
    userform = UserCreationForm(request.POST)
    if request.user.is_superuser:
        produc = Productos.objects.get(id = pk)
        posts = Productos.objects.all()
        marca = Marca.objects.all()


        formulario = ProductosForm(request.POST or None, instance=produc)

        if request.method == 'POST' and formulario.is_valid():

            formulario.save()
            return render(request, 'tienda/listado.html', {'posts': posts})

        return render(request, 'tienda/edicion.html', {'formulario' : formulario, 'produc':produc, 'posts':marca})
    else:
        return render(request, 'registration/registro.html', {"form": userform})


#Creamos un metrodo el cual recibe el request y el id del producto que queremos eliminar
#@user_passes_test(lambda u: u.is_superuser)
def eliminar(request, pk):
    userform = UserCreationForm(request.POST)
    if request.user.is_superuser:
        #devolvemos el producto a traves del id que le hemos pasado
        produc = Productos.objects.get(id=pk)
        posts = Productos.objects.all()
        produc.delete()
        return render(request, 'tienda/listado.html', {'posts': posts})
    else:
        return render(request, 'registration/registro.html', {"form": userform})
#@user_passes_test(lambda u: u.is_superuser)
def nuevo(request):
    formulario = ProductosForm(request.POST or None)
    posts = Productos.objects.all()
    marca = Marca.objects.all()

    if formulario.is_valid():
        formulario.save()
        return render(request, 'tienda/listado.html', {'posts': posts})
    return render(request, 'tienda/nuevo.html', {'formulario':formulario, 'posts':marca})

def logear(request):

    if request.method=='POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasena)

            if user is not None:
                login(request, user)
                messages.info(request, f'Estas logueado como {usuario}')
                return redirect('tienda:welcome')
            else:
                messages.error(request, 'Usuario o contraseña equivocada')
        else:
            messages.error(request, 'Usuario o contraseña equivocada')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})

def registrar(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        usuario = form.save()
        nombre_usuario= form.cleaned_date.get('username')
        messages.success(request, f'Nueva Cuenta Creada: {nombre_usuario}')
        login(request, usuario)
        messages.info(request,f'Has sido logueado como {nombre_usuario}')
        return render(request, 'tienda/index.html', {})
    else:
        for msg in form.error_messages:
            messages.error(request, f'{msg}: form.error_messages[msg]')
    form = UserCreationForm
    return render(request, 'registration/registro.html',{"form":form})

def cerrarsesion(request):
    logout(request)
    return render(request, 'tienda/index.html')

