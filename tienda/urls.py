from django.urls import path
from . import views


urlpatterns = [
    path('tienda/admin/actualizado/', views.actualizado, name='actualizado'),
    path('tienda/admin/listado/', views.listado_producto, name='listado'),
    path('tienda/admin/edicion/<int:pk>', views.editar, name='editar'),
    path('tienda/admin/eliminar/<int:pk>', views.eliminar, name='eliminar'),
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),

]
