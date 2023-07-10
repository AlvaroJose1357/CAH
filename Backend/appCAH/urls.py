from django.urls import path
from . import views 

urlpatterns =[
    path('',views.inicio),
    path('oferta/',views.oferta),
    path('oferta/registrar',views.registrarOferta),
    path('oferta/modificar',views.modificarOferta),
    path('vehiculo/',views.vehiculo),
    path('vehiculo/registrar',views.registrarVehiculo),
    path('vehiculo/modificar',views.modificarVehiculo),
]