
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from AppCarrito.carrito import Carrito

from .models import Order, OrderItem

def verificar(request, primer_nombre, apellido, email, address, codigopostal, lugar, telefono, monto):
    order = Order.objects.create(primer_nombre=primer_nombre, apellido=apellido, email=email, address=address, codigopostal=codigopostal, lugar=lugar, telefono=telefono, monto=monto)

    for item in Carrito(request):
        OrderItem.objects.create(order=order, producto=item['producto'], usuario=item['producto'].usuario, precio=item['producto'].precio, quantity=item['quantity'])
        
        order.usuarios.add(item['producto'].usuario)

    return order


def notify_vendor(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    for usuario in order.usuarios.all():
        to_email = usuario.propietario.email
        subject = 'Nueva Orden'
        text_content = 'Tienes una nueva orden de compra!'
        html_content = render_to_string('order/email_notify_vendor.html', {'order': order, 'usuario': usuario})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

def notify_customer(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    to_email = order.email
    subject = 'Confirmación de orden'
    text_content = 'Gracias por tu compra!'
    html_content = render_to_string('order/email_notify_customer.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()