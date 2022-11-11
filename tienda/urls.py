from django.urls import path
from . import views

app_name='tienda'
urlpatterns = [
    path('loginout/', views.cerrarsesion, name="loginout"),
    path('registro/', views.registrar, name="registro"),
    path('login/', views.logear, name="login"),
    path('tienda/admin/nuevo/', views.nuevo, name='nuevo'),
    path('tienda/admin/listado/', views.listado_producto, name='listado'),
    path('tienda/admin/edicion/<int:pk>', views.editar, name='editar'),
    path('tienda/admin/eliminar/<int:pk>', views.eliminar, name='eliminar'),
    path('', views.welcome, name='welcome',),
    path('tienda/', views.welcome, name='welcome'),

]
