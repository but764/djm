from django.shortcuts import render


def main(request):
    title = 'Магазин'

    context = {
        'title': title,
    }
    return render(request, 'djshop/index.html', context)


def contacts(request):
    title = 'Контакты'

    context = {
        'title': title
    }

    return render(request, 'djshop/contact.html', context)