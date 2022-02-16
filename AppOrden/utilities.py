from AppCarrito.carrito import Carrito

from .models import Orden, OrdenItem

def verificar(request, primer_nombre, apellido, email, address, codigopostal, lugar, telefono, monto):
    orden = Orden.objects.create(primer_nombre=primer_nombre, apellido=apellido, email=email, address=address, codigopostal=codigopostal, lugar=lugar, telefono=telefono, monto=monto)

    for item in Carrito(request):
        OrdenItem.objects.create(orden=orden, producto=item['producto'], usuario=item['producto'].usuario, precio=item['producto'].precio, quantity=item['producto'])
        
        orden.usuario.add(item['producto'].usuario)

    return orden