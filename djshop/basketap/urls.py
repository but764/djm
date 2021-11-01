from django.urls import path
import basketap.views as basketap

app_name = 'basketap'

urlpatterns = [
    path('', basketap.basket, name='view'),
    path('add/<int:pk>/', basketap.basket_add, name='add'),
    path('remove/<int:pk>/', basketap.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketap.basket_edit, name='edit')
]