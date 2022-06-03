from django import views
from . import views
from django.urls import path

# urls
urlpatterns=[
    path('',views.home,name='home'),
    path('stockin',views.stock_in,name='stockin'),
    path('stockout',views.stock_out,name='stockout'),
    path('no-order',views.no_order,name='no_order'),
    path('payment_pending',views.payment_pending,name='payment_pending'),
]