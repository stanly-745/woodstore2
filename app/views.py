from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'app/index.html')

def stock_in(request):
    return render(request,'app/stock_in.html')

def stock_out(request):
    return render(request,'app/stock_out.html')

def payment_pending(request):
    return render(request,'app/payment_pending.html')

def no_order(request):
    return render(request,'app/no_order.html')