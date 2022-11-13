from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from tienda.models import Productos, Marca
from .forms import ProductosForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q

from django.contrib.auth.models import User


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html',)



#@user_passes_test(lambda u: u.is_superuser)
def listado_producto(request):
    if request.user.is_superuser:
        posts = Productos.objects.all()
        return render(request, 'tienda/listado.html', {'posts': posts})
    else:
        return redirect('tienda:registro')




#Creamos un metodo el cual modifica el producto que nos pasan como parametro
@user_passes_test(lambda u: u.is_superuser)
def editar(request, pk):
    userform = UserCreationForm(request.POST)
    if request.user.is_superuser:
        produc = Productos.objects.get(id = pk)
        posts = Productos.objects.all()
        marca = Marca.objects.all()


        formulario = ProductosForm(request.POST or None, instance=produc)

        if request.method == 'POST' and formulario.is_valid():

            formulario.save()
            return redirect('tienda:listado')

        return render(request, 'tienda/edicion.html', {'formulario' : formulario, 'produc':produc, 'posts':marca})
    else:
        return render(request, 'registration/registro.html', {"form": userform})





#Creamos un metrodo el cual recibe el request y el id del producto que queremos eliminar
@user_passes_test(lambda u: u.is_superuser)
def eliminar(request, pk):
    userform = UserCreationForm(request.POST)
    if request.user.is_superuser:
        #devolvemos el producto a traves del id que le hemos pasado
        produc = Productos.objects.get(id=pk)
        posts = Productos.objects.all()
        produc.delete()
        return redirect('tienda:listado')
    else:
        return render(request, 'registration/registro.html', {"form": userform})



@user_passes_test(lambda u: u.is_superuser)
def nuevo(request):
    formulario = ProductosForm(request.POST or None)
    posts = Productos.objects.all()
    marca = Marca.objects.all()

    if formulario.is_valid():
        formulario.save()
        return redirect('tienda:listado')
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
    data = {
        'form': UserCreationForm(request.POST)
    }
    if request.method=='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request,'Te has registrado correctamente')
            return redirect('tienda:welcome')
        else:
            for msg in formulario.error_messages:
                messages.error(request, formulario.error_messages[msg])
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)



def cerrarsesion(request):
    logout(request)
    messages.info(request, "Se cerró sesión")
    return redirect('tienda:welcome')


def compras(request):
    if request.user.is_superuser:
        busqueda = request.GET.get('buscar')#Traeme el contenido que tenga en el form con el name='buscar'
        posts = Productos.objects.all()

        if busqueda:
            posts = Productos.objects.filter(
                Q(nombre__icontains=busqueda) |
                Q(marca__nombre__icontains=busqueda)#__icontains lo que hace es q no busque exactamente lo que pongamos
            ).distinct()
        return render(request, 'compras/compra.html', {'posts': posts} )
    else:
        return redirect('tienda:registro')

def checkout(request, id):

    produc = Productos.objects.get(id=id)
    return render(request, 'compras/checkout.html', {'post':produc} )




