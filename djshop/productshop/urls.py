from django.urls import path
from .views import products

app_name = 'productshop'

urlpatterns = [
    path('', products, name='main'),
    path('category/<int:pk>', products, name='category'),
]
