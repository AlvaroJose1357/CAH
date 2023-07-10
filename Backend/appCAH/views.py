from django.shortcuts import render
# Create your views here.



'''def vehiculo(request):
    return render(request,"Frontend/Vehiculo/vehiculo.html")
def conductor(request):
    return render(request,"Frontend/Conductor/condu.html")
def bodega(request):
    return render(request,"Frontend/Bodega/bodega.html")
def agricultor(request):
    return render(request,"Frontend/Agricultor/agri.html")
def producto(request):
    return render(request,"Frontend/Producto/producto.html")
def oferta(request):
    return render(request,"")
def mayorista(request):
    return render(request,"")'''

def inicio(request):
  return render(request, 'Inicio/index.html')

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