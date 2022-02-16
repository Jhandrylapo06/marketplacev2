from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    fechadecreacion = models.DateTimeField(auto_now_add=True)
    propietario = models.OneToOneField(User, related_name='usuario', on_delete=models.CASCADE) 
    
    class Meta:
        ordering= ['nombre']

    def __str__(self):
        return self.nombre

    def get_balance(self):
        items = self.items.filter(usuariopagado=False, order__usuarios__in=[self.id])
        return sum((item.producto.precio * item.quantity) for item in items)
    
    def get_paid_amount(self):
        items = self.items.filter(usuariopagado=True, order__usuarios__in=[self.id])
        return sum((item.producto.precio * item.quantity) for item in items)