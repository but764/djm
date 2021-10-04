from django.shortcuts import render


def main(request):
    return render(request, 'djshop/index.html')


def contacts(request):
    return render(request, 'djshop/contact.html')