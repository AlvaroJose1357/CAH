from django.contrib import admin
from .models import Perfil,Usuario, Bodega,Conductor,Vehiculo,Agricultor,Producto,ProductoCategoria,Oferta,Mayorista,MetodoPago,Carrito,CarritoOferta
admin.site.register(Perfil)
admin.site.register(Usuario)
admin.site.register(Bodega)
admin.site.register(Conductor)
admin.site.register(Vehiculo)
admin.site.register(Agricultor)
admin.site.register(Producto)
admin.site.register(ProductoCategoria)
admin.site.register(Oferta)
admin.site.register(Carrito)
admin.site.register(CarritoOferta)
admin.site.register(Mayorista)
admin.site.register(MetodoPago)
# Register your models here.
