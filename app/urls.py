from django import views
from . import views
from django.urls import path

# urls
urlpatterns=[
    path('',views.home,name='home'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('worker/<str:pk>/',views.worker,name='worker'),
    path('stockin',views.stock,name='stock'),
    path('order_history',views.order_history,name='order-his'),
    path('products',views.product,name='product'),
    path('order',views.order,name='order'),
    path('addcustomer',views.customerform,name='addcustomer'),
    path('addworker',views.workerform,name='addworker'),
    path('addproduct',views.productform,name='addproduct'),
    path('addstock',views.stockform,name='addstock'),
    path('addorder',views.orderform,name='addorder'),
    path('update-order/<str:pk>/',views.update_order,name='up-order'),
    path('update-stock/<str:pk>/',views.update_stock,name='up-stock'),
    path('bill/add/',views.billgeneration,name='bill-add'),
    path('bill/sum/<int:pk>',views.calcsum,name='calc-sum'),
    path('bill/<int:pk>',views.billdetail,name='bill-detail'),
    path('add-product-in-bill/<int:pk>/',views.bill_prod_add,name='add-bill-product'),
    path('expence/',views.expense,name='expence')
]