from django.shortcuts import render

# Create your views here.
def inicio(request):
  return render(request, 'Inicio/index.html')

def OpcionesUsuario(request):
  return render(request, 'UsuarioGlobal/usuario_global.html')

def login(request):
  return render(request, 'login/login.html')

def registrarse(request):
  return render(request, 'login/registrarse.html')

def oferta(request):
  return render(request, 'Oferta/oferta.html')

def registrarOferta(request):
  return render(request, 'Oferta/registrar-oferta.html')

def modificarOferta(request):
  return render(request, 'Oferta/modificar-oferta.html')

def vehiculo(request):
  return render(request, 'Vehiculo/vehiculo.html')

def registrarVehiculo(request):
  return render(request, 'Vehiculo/registrar-vehiculo.html')

def modificarVehiculo(request):
  return render(request, 'Vehiculo/modificar-vehiculo.html')
