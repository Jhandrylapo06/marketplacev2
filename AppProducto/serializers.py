from rest_framework import serializers
from .models import Producto

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields = ['categoria', 'titulo', 'descripcion', 'precio','imagen']