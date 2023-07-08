from django.db import models

# Create your models here.
class Perfil(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion= models.CharField(max_length=100)
    tipoPerfil= models.CharField(max_length=100)

class Usuario(models.Model):
    nombre1= models.CharField(max_length=100)
    nombre2= models.CharField(max_length=100)
    apellido1= models.CharField(max_length=100)
    apellido2= models.CharField(max_length=100)
    email= models.EmailField(max_length=200)
    contrasenia= models.CharField(max_length=50)
    telefono= models.CharField(max_length=50)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

class Bodega(models.Model):
    tipo_bodega =models.CharField(max_length=200)
    capacidad=models.IntegerField()
    id_usuario =models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Conductor(models.Model):
    id_usuario =models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Vehiculo(models.Model):
    placa = models.CharField(max_length=20)
    capacida_vehiculo = models.IntegerField()
    documentacion = models.IntegerField()
    tipo_vehiculo = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=500)
    id_conductor =models.ForeignKey(Conductor,on_delete=models.CASCADE)

class Agricultor(models.Model):
    id_usuario =models.ForeignKey(Usuario,on_delete=models.CASCADE)

class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=500)

class Producto(models.Model):
    nombre = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=500)
    id_producto_categoria =models.ForeignKey(ProductoCategoria,on_delete=models.CASCADE)

class Oferta(models.Model):
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    id_producto =models.ForeignKey(Producto,on_delete=models.CASCADE)
    id_agricultor =models.ForeignKey(Agricultor ,on_delete=models.CASCADE)
 
class Mayorista(models.Model):
    nombreEmpresa = models.CharField(max_length=100)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class MetodoPago(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

class Carrito(models.Model):
     cantidad = models.IntegerField()
     fechaVenta = models.DateField()
     fechaEntrega = models.DateField()
     costoTotal = models.IntegerField()
     cod_metodoPago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
     idMayorita = models.ForeignKey(Mayorista, on_delete=models.CASCADE)

class CarritoOferta(models.Model):
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    id_oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)


