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

def agricultor(request):
  return render(request, 'Vehiculo/agricultor.html')

def registrarAgricultor(request):
  return render(request, 'Agricultor/registrar-agricultor.html')

def modificarAgricultor(request):
  return render(request, 'Agricultor/modificar-agricultor.html')

def mayorista(request):
  return render(request, 'Mayorista/mayorista.html')

def registrarMayorista(request):
  return render(request, 'Mayorista/registrar-mayorista.html')

def modificarMayorista(request):
  return render(request, 'Mayorista/modificar-mayorista.html')

def conductor(request):
  return render(request, 'Conductor/conductor.html')

def registrarConductor(request):
  return render(request, 'Conductor/registrar-conductor.html')

def modificarConductor(request):
  return render(request, 'Conductor/modificar-conductor.html')

def bodega(request):
  return render(request, 'Bodega/bodega.html')

def registrarBodega(request):
  return render(request, 'Bodega/registrar-bodega.html')

def modificarBodega(request):
  return render(request, 'Bodega/modificar-bodega.html')

def producto(request):
  return render(request, 'Producto/producto.html')

def registrarProducto(request):
  return render(request, 'Producto/registrar-producto.html')

def modificarProducto(request):
  return render(request, 'Producto/modificar-producto.html')

def vehiculo(request):
  return render(request, 'Vehiculo/vehiculo.html')

def registrarVehiculo(request):
  return render(request, 'Vehiculo/registrar-vehiculo.html')

def modificarVehiculo(request):
  return render(request, 'Vehiculo/modificar-vehiculo.html')

def oferta(request):
  return render(request, 'Oferta/oferta.html')

def registrarOferta(request):
  return render(request, 'Oferta/registrar-oferta.html')

def modificarOferta(request):
  return render(request, 'Oferta/modificar-oferta.html')


