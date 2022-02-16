from django.shortcuts import render

# Create your views here.
from AppProducto.models import Producto

def Principal_view(request):

    newest_productos = Producto.objects.all()[0:8]
    return render(request,'home/Principal.html',{'newest_productos': newest_productos})

def Contacto_view(request):
    return render(request,'home/Contacto.html')