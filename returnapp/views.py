from django.shortcuts import render,redirect
from productapp.models import Product
from django.contrib import messages
from customerapp.models import Customer
from django.http import JsonResponse
from accounts.models import User
from sellapp.models import *
from decimal import Decimal
from utility.render_to_pdf import generate_pdf
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponse
from accounts.unique_uuid import unique_code
from depositapp.models import Payment
from django.utils.timezone import datetime,timedelta


# Create your views here.

def return_list(request):
    orders = Order.objects.all()

    data ={
        'orders':orders,
    }

    return render(request, 'admin/super/return/list.html',data)


def return_detail(request,id):
    order = Order.objects.get(id=id)
    products = ProductOrder.objects.filter(orderID=order)
    customer = CustomerOrder.objects.filter(orderID=order).first()
    #CustomerOrder

    data ={
        'products':products,
        'customer':customer,
        'order':order,
    }
    return render(request, 'admin/super/return/detail.html',data)


def return_filter_return(request):
    order_filter =  request.POST['order_filter']
    today = datetime.today()
    if order_filter == 'day':
        output = 'Day'
        orders = Order.objects.filter(created_at__date=today).order_by('id')

    if order_filter == 'month':
        output = 'Month'
        orders = Order.objects.filter(created_at__month=today.month).order_by('id')

    if order_filter == 'year':
        output = 'Year'
        orders = Order.objects.filter(created_at__year=today.year).order_by('id')

    if order_filter == 'all':
        output = 'All'
        orders = Order.objects.all()

    if order_filter == 'date_to_date':
        startdate =  request.POST['start_date']
        enddate =  request.POST['end_date']
        output = startdate + ' to '+ enddate

        orders = Order.objects.filter(created_at__range=[startdate, enddate]).order_by('id')

    data ={
        'orders':orders,
        'output':output,
    }

    return render(request, 'admin/super/return/list.html',data)

def return_post(request):
    productIDTest = request.POST.getlist('productID')
    productID = request.POST.getlist('productID')
    unit = request.POST.getlist('unit')
    unitTest = request.POST.getlist('unit')
    orderID =  request.POST['orderID']
    # print(productID)
    # print(unit)

    order = Order.objects.get(id=orderID )

    mySubtotal = 0

    for productID,unit in zip(productID,unit):
        productOrder = ProductOrder.objects.get(id=productID)
        afterInt = int(unit)
        if afterInt > productOrder.unit:
            messages.warning(request, "Return Value Upper")
            return redirect('return-detail',orderID)
        # print(productID)
        # print(productOrder.unit)
        # print(unit)


    for productID,unit in zip(productIDTest,unitTest):
        print(productID)
        productOrder = ProductOrder.objects.get(id=productID)
        afterInt = int(unit)
        # print(productOrder.sellPrice)
        mySubtotal = mySubtotal+(afterInt *productOrder.sellPrice)
        updateUnit = productOrder.unit - afterInt
        ProductOrder.objects.filter(id=productOrder.id).update(unit=updateUnit)
        # print(productID)
        # print(productOrder.sellPrice)
        # print(unit)
    
    # print(updateSubtotal)
    
    updateVat = (order.vatParcent / 100) * mySubtotal
    updateDiscount = (order.discountParcent / 100) * mySubtotal
    updateTotal = (mySubtotal+updateVat) -updateDiscount
    # print(updateTotal)
    calVat = order.vat - updateVat
    calDiscount = order.discount - updateDiscount
    calSub = order.subPrice - mySubtotal
    calTotal = order.totalPrice - updateTotal

    returnTime = order.returnTime +1
    Order.objects.filter(id=orderID ).update(vat=calVat,discount=calDiscount,subPrice=calSub,totalPrice=calTotal,returnTime=returnTime)
    messages.success(request, "Return successfully")
    
    return redirect('return-detail',orderID)

 

