from django.contrib import admin

from productshop.models import ProductCategory, Product

admin.site.register(ProductCategory)
admin.site.register(Product)