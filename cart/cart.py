from decimal import Decimal
from django.conf import settings

from shop.models import Product


class Cart(object):
    def __init__(self, request):
        """ Inicializaciya obyekta korziny."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Sohranyayem v sessii pustuyu korzinu.
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """Dobavleniye tovara v korzinu ili obnovleniye ego kolichestva."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Pomechayem sessiyu kak izmenennuyu
        self.session.modified = True

    def remove(self, product):
        """ Udaleniye tovara iz korziny"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """ Prohodim po tovaram korziny i poluchayem sootvetstvuyushiye obyekty Product."""
        product_ids = self.cart.keys()
        # Poluchayem obyekty modeli Product i peredyaem ih v korzinu.
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """ Vozvrashayet obsheye kolichestvo tovarov v korzine."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item['price']) * item['quantity']
                    for item in self.cart.values()
        )
    
    def clear(self):
        # Ochistka korziny.
        del self.session[settings.CART_SESSION_ID]
        self.save()