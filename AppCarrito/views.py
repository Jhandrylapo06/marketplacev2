import stripe

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render


from .carrito import Carrito
from .forms import VerificacionForm
from AppOrder.utilities import verificar, notify_vendor, notify_customer


# Create your views here.
def CarritoDetalles_view(request):
    carrito = Carrito(request)

    if request.method == 'POST':
        form = VerificacionForm(request.POST)

        if form.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY

            stripe_token = form.cleaned_data['stripe_token']

            try:
                    
                charge = stripe.Charge.create(
                    amount=int(carrito.get_total_cost() * 100),
                    currency='USD',
                    description='Charge from MarketPlace',
                    source=stripe_token
                )

                primer_nombre = form.cleaned_data['primer_nombre']
                apellido = form.cleaned_data['apellido']
                email = form.cleaned_data['email']
                telefono = form.cleaned_data['telefono']
                address = form.cleaned_data['address']
                codigopostal = form.cleaned_data['codigopostal']
                lugar = form.cleaned_data['lugar']

                order = verificar(request, primer_nombre, apellido, email, address, codigopostal, lugar, telefono, carrito.get_total_cost())

                carrito.clear()

                notify_customer(order)
                notify_vendor(order)

                return redirect('Correcto_view')
            except Exception:
                messages.error(request,'Hubo un error con el pago, reintente luego')
            
    else:
        
        form = VerificacionForm()

    removerdecarrito = request.GET.get('removerdecarrito','')
    cambiarcantidad = request.GET.get('cambiarcantidad','')
    quantity = request.GET.get('quantity', 0)

    if removerdecarrito:
        carrito.remove(removerdecarrito)

        return redirect('CarritoDetalles_view')

    if cambiarcantidad:
        carrito.add(cambiarcantidad, quantity, True)
        return redirect('CarritoDetalles_view')

    return render(request, 'carrito/Carrito.html', {'form': form, 'stripe_pub_key':settings.STRIPE_PUB_KEY})


def Correcto_view(request):
    return render(request, 'carrito/Correcto.html')