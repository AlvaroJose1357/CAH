from django.shortcuts import render, redirect
from . import forms, models
from django.http import HttpResponse
from django.urls import reverse
import ast

# Create your views here.

# Vista inicio ----------------------------------------------------------------------------------------

def inicio(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    return render(request, 'Inicio/index.html',{
      'rol': valores['rol']
    })
        
  else:
    return render(request, 'Inicio/index.html')


# Vista Opciones Usuario ----------------------------------------------------------------------------------------

def OpcionesUsuario(request):
  return render(request, 'UsuarioGlobal/usuario_global.html')

def login(request):
  if request.method == 'GET':
    return render(request, 'login/login.html', {
        'form' : forms.IniciarSesion()
      })
  else:
    try:
      usuario = models.Usuario.objects.get(numero_cedula=request.POST['numeroCedula'])
      print(usuario.contrasenia, request.POST['password'])
      print(type(request.POST['numeroCedula']))
      if request.POST['password'] == usuario.contrasenia and request.POST['email'] and usuario.email:
        # Almacenar la cookie del usuario, esto para conocer que tiene sesion iniciada
        valoresCookies={
          'id': usuario.id,
          'numeroCedula': usuario.numero_cedula,
          'rol': usuario.perfil.nombre.lower(),
        }

        response = redirect('inicio')
        response.set_cookie('user_id', valoresCookies, max_age=3600)

        return response
      
      else:
        return render(request, 'login/login.html', {
          'form' : forms.IniciarSesion(),
          'usuario': "Datos incorrectos"
        })
    except :
      # Manejo de la excepción cuando no se encuentra ningún usuario con esa cédula
      return render(request, 'login/login.html', {
          'form' : forms.IniciarSesion(),
          'usuario': "Usuario no existente"
        })
      

def registrarse(request):
  return render(request, 'login/registrarse.html')

# Vistas Agricultor ----------------------------------------------------------------------------------------

def agricultor(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    return render(request, 'Agricultor/agricultor.html',{
      'rol': valores['rol']
    })
        
  else:
    return render(request, 'Inicio/index.html')

def registrarAgricultor(request):
  if request.method == 'GET':
    return render(request, 'Agricultor/registrar-agricultor.html',{
      'form' : forms.RegistrarUsuario()
    })
  else:
    try:
      usuario = models.Usuario.objects.get(numero_cedula=request.POST['numeroCedula'])
      return render(request, 'Agricultor/registrar-agricultor.html', {
          'form' : forms.RegistrarUsuario(),
          'usuario': "Este usuario ya existe"
        })
    except:
      # Registra el usuario
      usuario= models.Usuario.objects.create(numero_cedula=request.POST['numeroCedula'], nombre1=request.POST['primerNombre'], nombre2=request.POST['segundoNombre'], apellido1=request.POST['primerpellido'], apellido2=request.POST['segundopellido'], email=request.POST['email'], contrasenia=request.POST['password'], telefono=request.POST['telefono'], perfil_id=1)
      # Lo registra como agricultor
      models.Agricultor.objects.create(id_usuario=usuario)
      
      # Almacenar la cookie del usuario, esto para conocer que tiene sesion iniciada
      valoresCookies={
        'id': usuario.id,
        'numeroCedula': usuario.numero_cedula,
        'rol': "agricultor",
      }

      response = redirect('inicio')
      response.set_cookie('user_id', valoresCookies, max_age=3600)

      return response


def modificarAgricultor(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    return render(request, 'Agricultor/modificar-agricultor.html',{
      'rol': valores['rol']
    })
  else:
    return render(request, 'Agricultor/modificar-agricultor.html')


# Vistas Mayorista ----------------------------------------------------------------------------------------

def mayorista(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    return render(request, 'Mayorista/mayorista.html',{
      'rol': valores['rol']
    })
        
  else:
    return render(request, 'Inicio/index.html')

def registrarMayorista(request):
  if request.method == 'GET':
    return render(request, 'Mayorista/registrar-mayorista.html',{
      'form' : forms.RegistrarMayorista()
    })
  else:
    try:
      usuario = models.Usuario.objects.get(numero_cedula=request.POST['numeroCedula'])
      return render(request, 'Mayorista/registrar-mayorista.html', {
          'form' : forms.RegistrarMayorista(),
          'usuario': "Este usuario ya existe"
        })
    except:
      # Registra el usuario
      usuario= models.Usuario.objects.create(numero_cedula=request.POST['numeroCedula'], nombre1=request.POST['primerNombre'], nombre2=request.POST['segundoNombre'], apellido1=request.POST['primerpellido'], apellido2=request.POST['segundopellido'], email=request.POST['email'], contrasenia=request.POST['password'], telefono=request.POST['telefono'], perfil_id=2)
      # Lo registra como agricultor
      models.Mayorista.objects.create(nombreEmpresa=request.POST['nombreEmpresa'] , idUsuario=usuario)
      
      # Almacenar la cookie del usuario, esto para conocer que tiene sesion iniciada
      valoresCookies={
        'id': usuario.id,
        'numeroCedula': usuario.numero_cedula,
        'rol': "mayorista",
      }

      response = redirect('inicio')
      response.set_cookie('user_id', valoresCookies, max_age=3600)

      return response

def modificarMayorista(request):
  return render(request, 'Mayorista/modificar-mayorista.html')


# Vista Conductor ----------------------------------------------------------------------------------------

def conductor(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    return render(request, 'Conductor/conductor.html',{
      'rol': valores['rol']
    })
        
  else:
    return render(request, 'Inicio/index.html')

def registrarConductor(request):
  if request.method == 'GET':
    return render(request, 'Conductor/registrar-conductor.html',{
      'form' : forms.RegistrarUsuario()
    })
  else:
    try:
      usuario = models.Usuario.objects.get(numero_cedula=request.POST['numeroCedula'])
      return render(request, 'Conductor/registrar-conductor.html', {
          'form' : forms.RegistrarUsuario(),
          'usuario': "Este usuario ya existe"
        })
    except:
      # Registra el usuario
      usuario= models.Usuario.objects.create(numero_cedula=request.POST['numeroCedula'], nombre1=request.POST['primerNombre'], nombre2=request.POST['segundoNombre'], apellido1=request.POST['primerpellido'], apellido2=request.POST['segundopellido'], email=request.POST['email'], contrasenia=request.POST['password'], telefono=request.POST['telefono'], perfil_id=3)
      # Lo registra como agricultor
      models.Conductor.objects.create(id_usuario=usuario)
      
      # Almacenar la cookie del usuario, esto para conocer que tiene sesion iniciada
      valoresCookies={
        'id': usuario.id,
        'numeroCedula': usuario.numero_cedula,
        'rol': "conductor",
      }

      response = redirect('inicio')
      response.set_cookie('user_id', valoresCookies, max_age=3600)

      return response

def modificarConductor(request):
  return render(request, 'Conductor/modificar-conductor.html')


# Vista Bodega ----------------------------------------------------------------------------------------

def bodega(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    return render(request, 'Bodega/bodega.html',{
      'rol': valores['rol']
    })
        
  else:
    return render(request, 'Inicio/index.html')

def registrarBodega(request):
  if request.method == 'GET':
    return render(request, 'Bodega/registrar-bodega.html',{
      'form' : forms.RegistrarBodega()
    })
  else:
    try:
      usuario = models.Usuario.objects.get(numero_cedula=request.POST['numeroCedula'])
      return render(request, 'Bodega/registrar-bodega.html', {
          'form' : forms.RegistrarBodega(),
          'usuario': "Este usuario ya existe"
        })
    except:
      # Registra el usuario
      usuario= models.Usuario.objects.create(numero_cedula=request.POST['numeroCedula'], nombre1=request.POST['primerNombre'], nombre2=request.POST['segundoNombre'], apellido1=request.POST['primerpellido'], apellido2=request.POST['segundopellido'], email=request.POST['email'], contrasenia=request.POST['password'], telefono=request.POST['telefono'], perfil_id=4)
      # Lo registra como agricultor
      models.Bodega.objects.create(tipo_bodega=request.POST['tipoBodega'],capacidad=request.POST['capacidad'] , id_usuario=usuario)
      
      # Almacenar la cookie del usuario, esto para conocer que tiene sesion iniciada
      valoresCookies={
        'id': usuario.id,
        'numeroCedula': usuario.numero_cedula,
        'rol': "bodega",
      }

      response = redirect('inicio')
      response.set_cookie('user_id', valoresCookies, max_age=3600)

      return response

def modificarBodega(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    return render(request, 'Bodega/modificar-bodega.html',{
      'rol': valores['rol']
    })
        
  else:
    return render(request, 'Inicio/index.html')


# Vista Producto ----------------------------------------------------------------------------------------

def producto(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    return render(request, 'Producto/producto.html',{
      'rol': valores['rol']
    })
        
  else:
    return render(request, 'Inicio/index.html')

def registrarProducto(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    return render(request, 'Producto/registrar-producto.html',{
      'rol': valores['rol']
    })
        
  else:
    return render(request, 'Producto/registrar-producto.html')

def modificarProducto(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    return render(request, 'Producto/modificar-producto.html',{
      'rol': valores['rol']
    })
        
  else:
    return render(request, 'Producto/modificar-producto.html')


# Vistas Vehiculo ----------------------------------------------------------------------------------------

def vehiculo(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    return render(request, 'Vehiculo/vehiculo.html',{
      'rol': valores['rol']
    })
        
  else:
    return render(request, 'Vehiculo/vehiculo.html')

def registrarVehiculo(request):
  return render(request, 'Vehiculo/registrar-vehiculo.html')

def modificarVehiculo(request):
  return render(request, 'Vehiculo/modificar-vehiculo.html')


# Vistas oferta ----------------------------------------------------------------------------------------

def oferta(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    ofertas = models.Oferta.objects.all()
    return render(request, 'Oferta/oferta.html',{
      'rol': valores['rol'],
      'ofertas':ofertas
    })
        
  else:
    return render(request, 'Inicio/index.html')

def registrarOferta(request):
  valores_cookie = request.COOKIES.get('user_id')
  if valores_cookie:
    valores = ast.literal_eval(valores_cookie)
    if request.method == 'GET':
      return render(request, 'Oferta/registrar-oferta.html',{
        'form' : forms.RegistrarOferta(),
        'rol': valores['rol']
      })
    else:
        # Registra la oferta
        oferta= models.Oferta.objects.create(precio=request.POST['precio'], cantidad=request.POST['cantidad'], id_producto=models.Producto.objects.get(nombre=request.POST['producto']),id_agricultor = models.Agricultor.objects.get(id_usuario= models.Usuario.objects.get(numero_cedula =valores['numeroCedula'])))
        return redirect( '/oferta/')

  else:
    return render(request, 'Inicio/index.html')

def modificarOferta(request):
  return render(request, 'Oferta/modificar-oferta.html')


