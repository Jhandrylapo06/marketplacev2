import random
from django import forms

from django.contrib import messages
from django.db.models import Q, query_utils
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AnadirAlCarritoForm
from .models import Categoria, Producto

from AppCarrito.carrito import Carrito


from rest_framework import viewsets
from .serializers import ProductoSerializers



class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class=ProductoSerializers



def Buscar_view(request):
    query = request.GET.get('query', '')
    productos = Producto.objects.filter(Q(titulo__icontains=query) | Q(descripcion__icontains=query))

    return render(request, 'product/Buscar.html', {'productos':productos, 'query':query})




def Producto_view(request, categoria_slug, producto_slug):
    
    carrito = Carrito(request) 

    producto = get_object_or_404(Producto, categoria__slug=categoria_slug, slug=producto_slug)
    
    if request.method == 'POST' :
        
        form = AnadirAlCarritoForm(request.POST)

        if form.is_valid():
            
            quantity = form.cleaned_data['quantity']
            
            carrito.add(producto_id=producto.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'El producto se añadio al carrito')

            return redirect('Producto_view', categoria_slug=categoria_slug, producto_slug=producto_slug)
        
    else:
        print('hola')
        form = AnadirAlCarritoForm()
        
        

    productos_similares = list(producto.categoria.productos.exclude(id=producto.id))

    if len(productos_similares) >= 4:
        productos_similares = random.sample(productos_similares, 4)
    
    return render(request, 'product/producto.html', {'form': form, 'producto': producto, 'productos_similares': productos_similares})

def Categoria_view(request, categoria_slug):
    categoria = get_object_or_404(Categoria, slug=categoria_slug)
    
    return render(request, 'product/Categoria.html', {'categoria': categoria})