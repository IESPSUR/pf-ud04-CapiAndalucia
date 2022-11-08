from django.urls import path
from . import views


urlpatterns = [
    path('tienda/admin/listado/', views.listado_producto, name = 'listado'),
    path('tienda/admin/edicion/<int:pk>', views.edicion, name='edicion'),
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),

]
