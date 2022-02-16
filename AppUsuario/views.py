from django.contrib.auth import login
from django.contrib.auth import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import request
from django.utils.text import slugify
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User

from .models import Usuario
from AppProducto.models import Producto

from .forms import ProductoForm
# Create your views here.

from rest_framework import viewsets
from .serializers import UsuarioSerializers

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UsuarioSerializers

def Usuario_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            usuario = Usuario.objects.create(nombre=user.username, propietario=user)

            return redirect('principal') 
    else:
        form = UserCreationForm()

    
    return render(request, 'user/Usuario.html', {'form': form})

@login_required

def UsuarioAdmin_view(request):
    usuario = request.user.usuario
    productos = usuario.productos.all()
    orders = usuario.orders.all()

    for order in orders:
        order.usuario_monto = 0
        order.usuario_montopagado = 0
        order.totalpagado = True

        for item in order.items.all():
            if item.usuario == request.user.usuario:
                if item.usuariopagado:
                    order.usuario_montopagado += item.get_total_price()
                else:
                    order.usuario_monto += item.get_total_price()
                    order.totalpagado = False


    return render(request, 'user/UsuarioAdmin.html',{'usuario':usuario, 'productos':productos, 'orders': orders})

@login_required
def AñadirProducto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)

        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user.usuario
            producto.slug = slugify(producto.titulo)
            producto.save()

            return redirect('usuarioadmin')
    else:
        form = ProductoForm()
    return render(request, 'user/añadirproducto.html', {'form':form})

@login_required
def EditarProducto_view(request, pk):
    usuario = request.user.usuario
    producto = usuario.productos.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance= producto)

        if form.is_valid():
            form.save()

            return redirect('usuarioadmin')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'user/EditarProducto.html',{'form':form, 'producto':producto})




@login_required
def EditarUsuario_view(request):
    usuario = request.user.usuario

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        email = request.POST.get('email', '')

        if nombre:
            usuario.propietario.email = email
            usuario.propietario.save()

            usuario.nombre = nombre
            usuario.save()

            return redirect('usuarioadmin')
    
    return render(request, 'user/EditarUsuario.html', {'usuario': usuario})

def vendors(request):
    vendors = Usuario.objects.all()

    return render(request, 'user/vendors.html', {'vendors': vendors})


def vendor(request, vendor_id):
    vendor = get_object_or_404(Usuario, pk=vendor_id)

    return render(request, 'user/vendor.html', {'vendor': vendor})