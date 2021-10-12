from django.shortcuts import render
from productshop.models import Product

def main(request):
    title = 'Магазин'

    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'djshop/index.html', context)


def contacts(request):
    title = 'Контакты'

    context = {
        'title': title
    }

    return render(request, 'djshop/contact.html', context)