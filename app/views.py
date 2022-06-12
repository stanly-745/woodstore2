from contextlib import redirect_stderr
from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

# home page 
def home(request):
    no_order=Order.objects.count()
    pending_order=Order.objects.filter(status='Not-Delivered').count()
    customer=Customer.objects.all()
    worker=Worker.objects.all()
    stock=Stock.objects.filter(quantity=0).count()
    bill=Bill.objects.all().count()
    context={'customer':customer,'worker':worker,'no_order':no_order,'pending_order':pending_order,'stock':stock,'bill':bill}
    return render(request,'app/index.html',context)

# customer page
def customer(request,pk):
    customers=Customer.objects.get(id=pk)
    context={'customer':customers}
    return render(request,'app/customer.html',context)

# worker page
def worker(request,pk):
    workers=Worker.objects.get(id=pk)
    context={'worker':workers}
    return render(request,'app/worker.html',context)

# stock in page
def stock(request):
    stock=Stock.objects.all()
    stocks=Stock.objects.filter(quantity=0).all()
    context={'stock':stock,'stocks':stocks}
    return render(request,'app/stock.html',context)

# order history
def order_history(request):
    orders=Order.objects.filter(status='Delivered').all()
    context={'orders':orders}
    return render(request,'app/order_history.html',context)

# order page
def order(request):
    orders=Order.objects.filter(status='Not-Delivered').all()
    context={'orders':orders}
    return render(request,'app/order.html',context)

# product page
def product(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'app/product.html',context)




# form view

# customer form
def customerform(request):
    form=CustomerForm()
    if request.method=='POST':
        print(request.POST)
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/customer_form.html',context)

# worker form
def workerform(request):
    form=WorkerForm()
    if request.method=='POST':
        print(request.POST)
        form=WorkerForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/worker_form.html',context)

# product form
def productform(request):
    form=ProductForm()
    if request.method=='POST':
        print(request.POST)
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/product_form.html',context)

# stock form
def stockform(request):
    form=StockForm()
    if request.method=='POST':
        print(request.POST)
        form=StockForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/stock_form.html',context)

# order form
def orderform(request):
    form=OrderForm()
    if request.method=='POST':
        print(request.POST)
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addorder')
    context={'form':form}
    return render(request,'app/order_form.html',context)


# update

# update order
def update_order(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('bill-add')
    context={'form':form}
    return render(request,'app/order_form.html',context)

# update stock
def update_stock(request,pk):
    stock=Stock.objects.get(id=pk)
    form=StockForm(instance=stock)
    if request.method=='POST':
        form=StockForm(request.POST,instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock')
    context={'form':form}
    return render(request,'app/stock_form.html',context)



def calcsum(request,pk):
    bill_obj=Bill.objects.get(bill_num=pk)
    products_set=bill_product.objects.filter(bill_item=bill_obj)
    total=5
    
    for product in products_set:
        price=product.billprod.price
        qty=product.quantity
        item_sum=price*qty
        total=total+item_sum
    bill_obj.total_sum=total
    bill_obj.save()
    return redirect('bill-detail',pk=bill_obj.bill_num)

def billgeneration(request):
    bill_obj=billform(request.POST)
    if bill_obj.is_valid():
       bills=bill_obj.save()
       return redirect('calc-sum',pk=bills.bill_num)
    return render(request,'app/billadd_form.html',{'form':billform})



def billdetail(request,pk):
    bill_obj=Bill.objects.get(bill_num=pk)
    bill_prds=bill_product.objects.filter(bill_item=bill_obj)
    context={
        'bill':bill_obj,
        'products':bill_prds
    }
    return render(request,'app/bill_detail.html',context)

def bill_prod_add(request,pk):
    billing_form=billproductform(request.POST)
    bill_obj=Bill.objects.get(bill_num=pk)
    if billing_form.is_valid():
        billform_obj=billing_form.save(commit=False)
        product_obj=billform_obj.billprod
        qty=billform_obj.quantity
        try :
            bill_info=bill_product.objects.get(bill_item=bill_obj,billprod=product_obj)
            bill_info.quantity=qty
            bill_info.save()
        except bill_product.DoesNotExist:
            bills=billing_form.save(commit=False)
            bills.bill_item=bill_obj
            bills.save()

        return redirect('calc-sum',pk=bill_obj.bill_num)
    return render(request,'app/billadd_form.html',{'form':billing_form})



# Expence view
def expense(request):
    expenses=Expense.objects.all()
    return render(request,'app/expense.html',{'expense':expenses})