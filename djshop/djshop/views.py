from django.shortcuts import render

from basketap.models import Basket
from productshop.models import Product

def main(request):
    title = 'Магазин'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        products = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': products,
        'basket': basket,
        'basket_count': basket,
    }
    return render(request, 'djshop/index.html', context)


def contacts(request):
    title = 'Контакты'

    context = {
        'title': title
    }

    return render(request, 'djshop/contact.html', context)