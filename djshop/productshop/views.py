from django.shortcuts import render

from productshop.models import ProductCategory


def products(request):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'productshop/products.html', context)


