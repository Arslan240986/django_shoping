from django.db import models
from shop.models import Product
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    first_name = models.CharField(_('Имя'), max_length=50)
    last_name = models.CharField(_('Фамилия'),max_length=50)
    email = models.EmailField(_('маил'))
    address = models.CharField(_('Адрес'), max_length=250)
    postal_code = models.CharField(_('Номер телефона'),max_length=20, blank=True)
    city = models.CharField(_('Город'),max_length=100,)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Ordera {}'.format(self.id)

    def get_products(self):
        return self.items.all()

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Список продуктов',
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, verbose_name='Цена', decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


