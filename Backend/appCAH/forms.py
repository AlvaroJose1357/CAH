from django import forms
from . import models

class RegistrarUsuario(forms.Form):
    numeroCedula = forms.CharField(label='',max_length=200, required=True,widget=forms.TextInput(attrs={'placeholder': 'Numero De Cedula'}))
    primerNombre = forms.CharField(label='',max_length=200,required=True, widget=forms.TextInput(attrs={'placeholder': 'Primer Nombre'}))
    segundoNombre = forms.CharField(label='',max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Segundo Nombre'}))
    primerpellido = forms.CharField(label='',max_length=200, required=True,widget=forms.TextInput(attrs={'placeholder': 'Primer Apellido'}))
    segundopellido = forms.CharField(label='',max_length=200, required=True ,widget=forms.TextInput(attrs={'placeholder': 'Segundo Apellido'}))
    email = forms.EmailField(label='',max_length=200, required=True, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    telefono = forms.CharField(label='',max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Numero De Telefono'}))

class RegistrarMayorista(forms.Form):
    numeroCedula = forms.CharField(label='',max_length=200, required=True,widget=forms.TextInput(attrs={'placeholder': 'Numero De Cedula'}))
    primerNombre = forms.CharField(label='',max_length=200,required=True, widget=forms.TextInput(attrs={'placeholder': 'Primer Nombre'}))
    segundoNombre = forms.CharField(label='',max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Segundo Nombre'}))
    primerpellido = forms.CharField(label='',max_length=200, required=True,widget=forms.TextInput(attrs={'placeholder': 'Primer Apellido'}))
    segundopellido = forms.CharField(label='',max_length=200, required=True ,widget=forms.TextInput(attrs={'placeholder': 'Segundo Apellido'}))
    email = forms.EmailField(label='',max_length=200, required=True, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    telefono = forms.CharField(label='',max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Numero De Telefono'}))
    nombreEmpresa = forms.CharField(label='',max_length=200,required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre De La Empresa'}))

class RegistrarBodega(forms.Form):
    numeroCedula = forms.CharField(label='',max_length=200, required=True,widget=forms.TextInput(attrs={'placeholder': 'Numero De Cedula'}))
    primerNombre = forms.CharField(label='',max_length=200,required=True, widget=forms.TextInput(attrs={'placeholder': 'Primer Nombre'}))
    segundoNombre = forms.CharField(label='',max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder': 'Segundo Nombre'}))
    primerpellido = forms.CharField(label='',max_length=200, required=True,widget=forms.TextInput(attrs={'placeholder': 'Primer Apellido'}))
    segundopellido = forms.CharField(label='',max_length=200, required=True ,widget=forms.TextInput(attrs={'placeholder': 'Segundo Apellido'}))
    email = forms.EmailField(label='',max_length=200, required=True, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    telefono = forms.CharField(label='',max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Numero De Telefono'}))
    tipoBodega = forms.CharField(label='',max_length=200,required=True, widget=forms.TextInput(attrs={'placeholder': 'Tipo De Bodega'}))
    capacidad = forms.CharField(label='',max_length=200,required=True, widget=forms.TextInput(attrs={'placeholder': 'Capacidad'}))

class RegistrarOferta(forms.Form):
    precio = forms.CharField(label='',max_length=200, required=True,widget=forms.TextInput(attrs={'placeholder': 'Precio (Kilo)'}))
    cantidad = forms.CharField(label='',max_length=200,required=True, widget=forms.TextInput(attrs={'placeholder': 'Cantidad (Kilos)'}))
    producto = forms.ModelChoiceField(label="", queryset=models.Producto.objects.values_list('nombre',flat=True), widget=forms.Select(attrs={'placeholder': 'Selecciona El producto'}))

    

class IniciarSesion(forms.Form):
    numeroCedula= forms.CharField(label='',max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Numero De Cedula'}))
    email = forms.EmailField(label='',max_length=200, required=True, widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))