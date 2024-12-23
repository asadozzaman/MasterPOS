from django.shortcuts import render,redirect
from sellapp.models import *
from depositapp.models import *
from datetime import date
from django.db.models import Count, Sum
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import HttpResponseRedirect
from django.contrib import auth, messages
from django.utils.timezone import datetime,timedelta

from shopapp.models import ProductROrder, ROrder, RetailerOrder

# Create your views here.


def admin_dashboard(request):
    today = date.today()


    sell = Order.objects.aggregate(Sum('totalPrice'))['totalPrice__sum']
    paid = Payment.objects.aggregate(Sum('amount'))['amount__sum']
    due = Order.objects.aggregate(Sum('duePrice'))['duePrice__sum']
    order = Order.objects.all().count()
    # sell = Order.objects.filter(created_at__date=today).aggregate(Sum('totalPrice'))['totalPrice__sum'] updated_at


    data = {
        'sell': sell,
        'paid': paid,
        'due': due,
        'order': order,
        # 'tests': reportTestinglist_c,
        }

    return render(request,  'admin/dashboard/index.html', data)

def admin_dashboard_filter(request):
    order_filter =  request.POST['order_filter']
    today = date.today()

    if order_filter == 'day':
        output = 'Day'
        sell = Order.objects.filter(created_at__date=today).aggregate(Sum('totalPrice'))['totalPrice__sum']
        paid = Payment.objects.filter(created_at__date=today).aggregate(Sum('amount'))['amount__sum']
        due = Order.objects.filter(created_at__date=today).aggregate(Sum('duePrice'))['duePrice__sum']
        order = Order.objects.filter(created_at__date=today).count()

    if order_filter == 'month':
        output = 'Month'
        sell = Order.objects.filter(created_at__month=today.month).aggregate(Sum('totalPrice'))['totalPrice__sum']
        paid = Payment.objects.filter(created_at__month=today.month).aggregate(Sum('amount'))['amount__sum']
        due = Order.objects.filter(created_at__month=today.month).aggregate(Sum('duePrice'))['duePrice__sum']
        order = Order.objects.filter(created_at__month=today.month).count()
        
    if order_filter == 'year':
        output = 'Year'
        sell = Order.objects.filter(created_at__year=today.year).aggregate(Sum('totalPrice'))['totalPrice__sum']
        paid = Payment.objects.filter(created_at__year=today.year).aggregate(Sum('amount'))['amount__sum']
        due = Order.objects.filter(created_at__year=today.year).aggregate(Sum('duePrice'))['duePrice__sum']
        order = Order.objects.filter(created_at__year=today.year).count()

    if order_filter == 'all':
        output = 'All'
        sell = Order.objects.aggregate(Sum('totalPrice'))['totalPrice__sum']
        paid = Payment.objects.aggregate(Sum('amount'))['amount__sum']
        due = Order.objects.aggregate(Sum('duePrice'))['duePrice__sum']
        order = Order.objects.all().count()

    if order_filter == 'date_to_date':

        startdate =  request.POST['start_date']
        enddate =  request.POST['end_date']

        output = startdate + ' to '+ enddate

        sell = Order.objects.filter(created_at__range=[startdate, enddate]).aggregate(Sum('totalPrice'))['totalPrice__sum']
        paid = Payment.objects.filter(created_at__range=[startdate, enddate]).aggregate(Sum('amount'))['amount__sum']
        due = Order.objects.filter(created_at__range=[startdate, enddate]).aggregate(Sum('duePrice'))['duePrice__sum']
        order = Order.objects.filter(created_at__range=[startdate, enddate]).count()


    data = {
        'sell': sell,
        'paid': paid,
        'due': due,
        'order': order,
        'output': output,
        # 'tests': reportTestinglist_c,
        }

    return render(request,  'admin/dashboard/index.html', data)



def all_order_list(request):
    orders = Order.objects.all()

    data ={
        'orders':orders,
    }

    return render(request, 'admin/super/allOrder/list.html',data)


def all_order_detail(request,id):
    order = Order.objects.get(id=id)
    products = ProductOrder.objects.filter(orderID=order)
    customer = CustomerOrder.objects.filter(orderID=order).first()
    #CustomerOrder

    data ={
        'products':products,
        'customer':customer,
        'order':order,
    }
    return render(request, 'admin/super/allOrder/detail.html',data)

def all_order_list_retailer(request):
    orders = ROrder.objects.all()

    data ={
        'orders':orders,
    }

    return render(request, 'admin/super/allRetailerOrder/list.html',data)


def all_order_detail_retailer(request,id):
    order = ROrder.objects.get(id=id)
    products = ProductROrder.objects.filter(orderID=order)
    customer = RetailerOrder.objects.filter(orderID=order).first()
    #CustomerOrder

    data ={
        'products':products,
        'customer':customer,
        'order':order,
    }
    return render(request, 'admin/super/allRetailerOrder/detail.html',data)



def profile(request):
    return render(request, 'admin/profile/profile.html')

def profile_change_password(request):
    return render(request, 'admin/profile/profile_change_password.html')

def profile_change_password_post(request):
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    try:
        validate_password(password)
        if password == cpassword:
            user = User.objects.get(id=request.user.id)
            print('fff',user)
            user.set_password(password)
            user.save()
            messages.success(request, 'Successfully Password Reset')
            return redirect('sign-in')
        else:
            messages.warning(request, 'Password not match')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except ValidationError as e:
        messages.warning(request, 'This password is too short. It must contain at least 8 characters.This password is too common.;This password is entirely numeric.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

    

def all_order_list_filter(request):
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

    return render(request, 'admin/super/allOrder/list.html',data)
    




