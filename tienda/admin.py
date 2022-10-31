from django.contrib import admin
import tienda.models

admin.site.register(tienda.models.Productos)
admin.site.register(tienda.models.Marca)
admin.site.register(tienda.models.Compra)
