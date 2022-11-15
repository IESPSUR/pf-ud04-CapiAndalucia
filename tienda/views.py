from datetime import datetime

from django.contrib import messages, auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction, connection
from django.shortcuts import render, redirect
from tienda.models import Productos, Marca, Compra
from .forms import ProductosForm, CustomUserCreationForm, CantidadCompra
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q

from django.contrib.auth.models import User

# Create your views here.
"""
View de la pagina inicial
"""


def welcome(request):
    return render(request, 'tienda/index.html', )


"""
View que nos muestra una lista de los productos para el administrador
"""


# @user_passes_test(lambda u: u.is_superuser)
def listado_producto(request):
    if request.user.is_superuser:
        posts = Productos.objects.all()
        return render(request, 'tienda/listado.html', {'posts': posts})
    else:
        return redirect('tienda:login')


"""
Creamos un metodo el cual modifica el producto que nos pasan como parametro
"""


def editar(request, pk):
    if request.user.is_superuser:
        produc = Productos.objects.get(id=pk)
        posts = Productos.objects.all()
        marca = Marca.objects.all()

        formulario = ProductosForm(request.POST or None, instance=produc)

        if request.method == 'POST' and formulario.is_valid():
            formulario.save()
            return redirect('tienda:listado')

        return render(request, 'tienda/edicion.html', {'formulario': formulario, 'produc': produc, 'posts': marca})
    else:
        return redirect('tienda:login')


"""
Creamos un metrodo el cual recibe el request y el id del producto que queremos eliminar
"""


def eliminar(request, pk):
    if request.user.is_superuser:
        # devolvemos el producto a traves del id que le hemos pasado
        produc = Productos.objects.get(id=pk)
        posts = Productos.objects.all()
        produc.delete()
        return redirect('tienda:listado')
    else:
        return redirect('tienda:login')


"""
Creamos un metodo el cual crea un nuevo producto en la base de datos
"""


def nuevo(request):
    if request.user.is_superuser:
        formulario = ProductosForm(request.POST or None)
        posts = Productos.objects.all()
        marca = Marca.objects.all()

        if formulario.is_valid():
            formulario.save()
            return redirect('tienda:listado')
        return render(request, 'tienda/nuevo.html', {'formulario': formulario, 'posts': marca})
    else:
        return redirect('tienda:login')


"""
Metodo que se usa para loguear al usuario
"""


def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
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
    return render(request, 'registration/login.html', {'form': form})


"""
Metodo que se usa para registrar a un nuevo usuario
"""


def registrar(request):
    data = {
        'form': UserCreationForm(request.POST)
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'],
                                password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Te has registrado correctamente')
            return redirect('tienda:welcome')
        else:
            for msg in formulario.error_messages:
                messages.error(request, formulario.error_messages[msg])
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)


"""
Metodo que cierra la sesion al usuario actual
"""


def cerrarsesion(request):
    logout(request)
    messages.info(request, "Se cerró sesión")
    return redirect('tienda:welcome')


"""
View de la pagina Compras que nos muestra una lista de productos y podemos filtrar esos productos
"""


@transaction.atomic
def compras(request):
    if request.user.is_authenticated:
        busqueda = request.GET.get('buscar')  # Traeme el contenido que tenga en el form con el name='buscar'
        posts = Productos.objects.all()

        if busqueda:
            posts = Productos.objects.filter(
                Q(nombre__icontains=busqueda) |
                Q(marca__nombre__icontains=busqueda)
                # __icontains lo que hace es q no busque exactamente lo que pongamos
            ).distinct()
        return render(request, 'compras/compra.html', {'posts': posts})
    else:
        return redirect('tienda:login')


"""
View que nos muestra los detalles de un producto y podemos comprar X unidades del producto
"""


@transaction.atomic
def checkout(request, id):
    if request.user.is_authenticated:
        produc = Productos.objects.get(id=id)
        form = CantidadCompra(request.POST)
        unit = int(request.GET.get('cantidad'))
        unidades = int(produc.unidades)
        cantidad = request.GET.get('cantidad')
        unit = int(cantidad)
        precio = int(unit) * produc.precio


        if request.method == 'POST':
            if unit < unidades:
                resultado = unidades - unit
                produc.unidades = resultado
                produc.save()

                compra = Compra(fecha=datetime.today().strftime('%Y-%m-%d'), unidades=unit,
                                importe=precio, producto=produc,
                                nombre_usuario=request.user)
                compra.save()

            return redirect('tienda:compras')

        return render(request, 'compras/checkout.html',{'post': produc, 'unidades': unit, 'precio': precio, 'valor': True})

    else:
        return redirect('tienda:login')


"""
View que miestra el informe de la pagina
"""


def informe(request):
    if request.user.is_superuser:

        marcas = Marca.objects.all()
        ventas = Compra.objects.all()
        ventas = ventas.order_by('-unidades')[:10]
        usuarios = User.objects.all()
        productos = Productos.objects.all()
        productos_ventas = Productos.objects.all()
        menu = request.GET.get('menu')
        top_product = Compra.objects.all().order_by('-unidades').prefetch_related('producto')
        cursor = connection.cursor()
        cursor.execute('select distinct tienda_productos.nombre from tienda_productos, tienda_compra where tienda_productos.id = tienda_compra.producto_id')
        top_product2 = cursor.fetchone()
        print(top_product2)

        top_product3 = Compra.objects.raw('select distinct tienda_productos.nombre, tienda_productos.id from tienda_productos, tienda_compra where tienda_productos.id = tienda_compra.producto_id')
        print(top_product3)

        for s in top_product3:
            print(s)


        if request.method == 'GET':

            if menu:
                productos = productos.filter(marca__nombre__icontains=menu)

                return render(request, 'tienda/informes.html', {'productos': productos, 'marcas': marcas, 'menu': menu, 'ventas':ventas, 'users':usuarios, 'top_productos':top_product3[:10]})

        if request.method == 'POST':
            productos2 = Productos.objects.all()
            elec = request.POST.get('usuario')

            print(usuarios)
            print(type(usuarios))
            if elec:
                productos2 = Compra.objects.all().filter(nombre_usuario__icontains=elec)

                return render(request, 'tienda/informes.html', {'productos': productos, 'usuario_compras':productos2, 'marcas': marcas, 'eleccion': elec, 'top_productos':top_product3[:10], 'ventas':ventas,'users':usuarios})
        return render(request, 'tienda/informes.html', {'productos': productos, 'marcas': marcas, 'ventas':ventas, 'users':usuarios})
    else:
        return redirect('tienda:login')


