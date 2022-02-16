from django.db import models

# Create your models here.
from AppProducto.models import Producto
from AppUsuario.models import Usuario

class Orden(models.Model):
    primer_nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100) 
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    codigopostal = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)  
    fechadecreacion = models.DateTimeField(auto_now_add=True) 
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    usuarios = models.ManyToManyField(Usuario, related_name='orders')

    class Meta:
        ordering = ['-fechadecreacion']

    def __str__(self) :
        return self.primer_nombre

class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='items', on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name='items', on_delete=models.CASCADE)
    usuariopagado = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self) :
        return self.id
