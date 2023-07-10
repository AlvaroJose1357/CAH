from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def hello(request):
    return HttpResponse("hello world")

def ejemnplorer(request):
    return render(request, "ejemplo.html")
def index(request):
    '''template = loader.get_template()
    
    
    return render(request,"Frontend/Inicio/index.html")
def vehiculo(request):
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
