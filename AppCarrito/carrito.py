from django.conf import settings

from AppProducto.models import Producto

class Carrito(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['producto'] = Producto.objects.get(pk=p)
        
        for item in self.cart.values():
            item['total_price'] = item['producto'].precio * item['quantity']

            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def add(self, producto_id, quantity=1, update_quantity=False):
        producto_id = str(producto_id)
        
        if producto_id not in self.cart:
            self.cart[producto_id] = {'quantity': 1, 'id': producto_id}
        
        if update_quantity:
            self.cart[producto_id]['quantity'] += int(quantity)

            if self.cart[producto_id]['quantity'] == 0:
                self.remove(producto_id)
                        
        self.save()
    
    def remove(self, producto_id):
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['producto'] = Producto.objects.get(pk=p)

        return sum(item['quantity'] * item['producto'].precio for item in self.cart.values())