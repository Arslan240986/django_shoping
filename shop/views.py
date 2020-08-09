import sys

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    if category_slug:

        category = get_object_or_404(Category, slug=category_slug)
        filter_products = products.filter(category=category)
        paginator = Paginator(filter_products, 4)
        page_obj = paginator.get_page(page)
    return render(request, 'shop/list.html',
                  {'category': category,
                   'categories': categories,
                   'page_obj': page_obj})


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, id=pk, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


print(sys.stdout.encoding)