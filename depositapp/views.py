from django.http import JsonResponse
from django.shortcuts import render,redirect
from customerapp.models import *
from sellapp.models import *
from depositapp.models import *
from decimal import Decimal
from django.contrib import messages
from django.http import HttpResponse
from utility.render_to_pdf import generate_pdf
from django.utils.timezone import datetime,timedelta

# Create your views here.




def deposit_amount_order_pdf(request,orderId,customerId):
    #pdf = generate_pdf('admin/super/pdf/report_pdf.html')

    customer = Customer.objects.get(unique_id=customerId)
    customerOrder = CustomerOrder.objects.filter(customerID=customer).first()
    order = Order.objects.get(id=orderId)
    productOrders = ProductOrder.objects.filter(orderID=orderId)


    pdf = generate_pdf('admin/super/deposit/pdf/deposit_pdf.html', {'order': order,'productOrders': productOrders,'customerOrder': customerOrder,'customer':customer})

    return HttpResponse(pdf, content_type='application/pdf')


# class ReportPDF(LoginRequiredMixin, View):
#     ''' This view will show lab tests pdf '''
#     def get(self, request):
#         Labreport = Customer.objects.all()
#         #reportTestinglist = ReportTestinglist.objects.filter(lab=Labreport.id)
#         # tests = Labreport.report_name.all()
#         #pdf = generate_pdf('admin/super/pdf/report_pdf.html', {'lab': Labreport})
#         pdf = generate_pdf('admin/super/pdf/report_pdf.html')
#         return HttpResponse(pdf, content_type='application/pdf')





def deposit_amount_post(request):

    amount = request.POST['amount']
    customerID = request.POST['customer_unique_id']
    orderID = request.POST['orderID']

    order = Order.objects.get(id=orderID)
    customer = Customer.objects.get(unique_id=customerID)
    decimelAMount = Decimal(amount)

    if order.duePrice < decimelAMount:
        messages.warning(request, "Higher Value!")
        return redirect('deposit-customer-detail', id=customer.unique_id)

    afterDue = order.duePrice - decimelAMount
     
    Order.objects.filter(id=orderID).update(duePrice=afterDue)



    payment= Payment()
    payment.orderID = order
    payment.customerID = customer
    payment.amount = amount
    payment.save()

    messages.success(request, "Payment Add Successfully!")
    return redirect('deposit-customer-detail', id=customer.unique_id)

   

def deposit_customer_list(request):

    customers = Customer.objects.all()

    data ={
        'customers':customers,
    }

    return render(request, 'admin/super/deposit/list.html',data)



def deposit_customer_detail(request,id):
    # return JsonResponse({'data': 'data'})
    customer = Customer.objects.get(unique_id=id)
    print(customer)
    orders = Order.objects.filter(customerID=customer)
    print('orders')
    print(orders)
    data ={
        'customer':customer,
        'orders':orders,
    }
    return render(request, 'admin/super/deposit/detail.html',data)

def deposit_payment_history(request):

    payments = Payment.objects.all()
    
    data ={
        'payments':payments,
    }

    return render(request, 'admin/super/payment/payment_history.html',data)

def deposit_order_list(request):

    orders = Order.objects.all()

    data ={
        'orders':orders,
    }

    return render(request, 'admin/super/deposit/orders_list.html',data)

def deposit_amount_order_post(request):
    amount = request.POST['amount']
    customerID = request.POST['customer_unique_id']
    orderID = request.POST['orderID']

    order = Order.objects.get(id=orderID)
    customer = Customer.objects.get(unique_id=customerID)
    decimelAMount = Decimal(amount)

    if order.duePrice < decimelAMount:
        messages.warning(request, "Higher Value!")
        return redirect('deposit-order-list')

    afterDue = order.duePrice - decimelAMount
     
    Order.objects.filter(id=orderID).update(duePrice=afterDue)



    payment= Payment()
    payment.orderID = order
    payment.customerID = customer
    payment.amount = amount
    payment.save()

    messages.success(request, "Payment Add Successfully!")
    return redirect('deposit-order-list')

def deposit_filter_deposit(request):
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

    return render(request, 'admin/super/deposit/orders_list.html',data)
    # print(order_filter)
    # return redirect('deposit-order-list')
