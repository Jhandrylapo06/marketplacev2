from django.forms import ModelForm, fields

from AppProducto.models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria','imagen','titulo','descripcion','precio']