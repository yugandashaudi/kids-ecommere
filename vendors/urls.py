from django.urls import path

from .views import *

urlpatterns=[
    path('create_product/',CreateProductView.as_view(),name='create_product'),
    path('get_ordered_product/',GetOrderView.as_view(),name='get_ordered_product'),
    path('create_order/',CreateOrderByCustomer.as_view(),name='create_order'),
    path('checkout/',CheckOutPage.as_view(),name='checkout')

]