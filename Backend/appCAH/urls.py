from django.urls import path
from . import views 

urlpatterns =[
    path('',views.inicio, name='inicio'),
    path('opciones-usuario/',views.OpcionesUsuario),
    path('login/',views.login),
    path('registrarse/',views.registrarse),
    path('agricultor/',views.agricultor, name='agricultor'),
    path('agricultor/registrar/',views.registrarAgricultor),
    path('agricultor/modificar/',views.modificarAgricultor),
    path('mayorista/',views.mayorista),
    path('mayorista/registrar/',views.registrarMayorista),
    path('mayorista/modificar/',views.modificarMayorista),
    path('conductor/',views.conductor),
    path('conductor/registrar/',views.registrarConductor),
    path('conductor/modificar/',views.modificarConductor),
    path('bodega/',views.bodega),
    path('bodega/registrar/',views.registrarBodega),
    path('bodega/modificar/',views.modificarBodega),
    path('producto/',views.producto),
    path('producto/registrar/',views.registrarProducto),
    path('producto/modificar/',views.modificarProducto),
    path('vehiculo/',views.vehiculo),
    path('vehiculo/registrar/',views.registrarVehiculo),
    path('vehiculo/modificar/',views.modificarVehiculo),
    path('oferta/',views.oferta, name='oferta'),
    path('oferta/registrar/',views.registrarOferta),
    path('oferta/modificar/',views.modificarOferta),
]