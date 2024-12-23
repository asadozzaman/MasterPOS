from django.shortcuts import render,redirect
from productapp.models import Product
from django.contrib import messages
from shopapp.models import *
from django.http import JsonResponse
from accounts.models import User
from decimal import Decimal
from utility.render_to_pdf import generate_pdf
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponse
from accounts.unique_uuid import unique_code

# Create your views here.

def sell_ajax_customer_info(request):
    offset = request.GET.get('offset')
    print(offset)
    customer =Retailer.objects.get(unique_id=offset)
    print(customer)

    # print(product)
    # print(product.id)
    # print(product.sellPrice)

    customersList = {
        'mobile_number':customer.user.mobile_number,
        'address':customer.user.address,
        'due':customer.due,
        'customerID':customer.unique_id,
        }


    data = {
        'customersList': customersList,
    }

    return JsonResponse({'data': data})




def sell_ajax_product_get(request):
    offset = request.GET.get('offset')
    # print(offset)
    product =Product.objects.get(id=offset)

    productsList = {
        'id':product.id,
        'name':product.name,
        'sellPrice':product.sellPrice,
        'stock':product.stock,
        'discount':product.discount,
        }


    data = {
        'productsList': productsList,
    }

    return JsonResponse({'data': data})


def sell_ajax_product_add(request):
     
    productID = request.GET.get('productID')
    totalQty = request.GET.get('totalQty')
    sellPrice = request.GET.get('sellPrice')
    totalDiscount = request.GET.get('totalDiscount')
    # print(productID)
    # print('totalQty',totalQty)
    # print('sellPrice',sellPrice)
    # print(productID)
    if totalQty == '':
        success = True
        message = "Please product & quantity added"
        response_data = {
        "success": success,
        "message": message
        }
        return JsonResponse(response_data)
    


    product =Product.objects.get(id=productID)

    print('totalQty',totalQty)
    print('stock',product.stock)
    inttotalQty = int(totalQty)

    # if inttotalQty > product.stock:
    #     success = True
    #     message = "Stock not available"
    #     response_data = {
    #     "success": success,
    #     "message": message
    #     }
    #     return JsonResponse(response_data)

    mytotalDiscount = float(totalDiscount)
    mysellPrice = float(sellPrice)

    sellsrate = mysellPrice * (mytotalDiscount / 100)


    mytotalQty = float(totalQty)
    discounted_price = mysellPrice - sellsrate

    totalSinglePrice = discounted_price * mytotalQty

    productsList = {
        'id':product.id,
        'name':product.name,
        'sellPrice':sellPrice,
        'totalQty':totalQty,
        'discount':totalDiscount,
        'totalSinglePrice':round(totalSinglePrice, 2),
        }


    data = {
        'productsList': productsList,
    }
    return JsonResponse({'data': data})


def sell_page(request):
    product = Product.objects.all()
    customers = Retailer.objects.all()

    data ={
        'product':product,
        'customers':customers,
    }


    return render(request, 'admin/super/buyProduct/buy.html',data)



def sell_add_post(request):
    productID = request.POST.getlist('productID')
    sellPrice = request.POST.getlist('sellPrice')
    totalQty = request.POST.getlist('totalQty')

    mobile_number =  request.POST['mobile_number']
    address =  request.POST['address']
    customerID =  request.POST['customerID']
    



    subPrice =  request.POST['subPrice']
    vatInput2 =  request.POST['vatInput2']
    discountInput2 =  request.POST['discountInput2']
    totalPrice =  request.POST['totalPrice']
    duePrice =  request.POST['duePrice']
    vat =  request.POST['vat']
    discount =  request.POST['discount']
    transport =  request.POST['transport']

    fields_to_check = [productID,sellPrice,totalQty,mobile_number,address,customerID,vatInput2,discountInput2,totalPrice,duePrice,vat,discount,transport]

    
    for field in fields_to_check:
        if field == '':
            print('ache')
            messages.warning(request, "Please fillup properly")
            return redirect('retailer-sell-page')
        else:
            print('naiiiii')

    customerID = Retailer.objects.get(unique_id=customerID)

    print('totalPricetotalPricetotalPrice',totalPrice)

    order = ROrder()
    order.unique_id = f'{unique_code(10)}'
    order.retailerID = customerID
    order.totalPrice =   Decimal(totalPrice)
    order.duePrice =  Decimal(duePrice)
    order.vat =  Decimal(vat)
    order.discount =  Decimal(discount)
    order.transport =  Decimal(transport)
    order.vatParcent =  Decimal(vatInput2)
    order.discountParcent =  Decimal(discountInput2)
    order.subPrice =  Decimal(subPrice)
    order.save()

    print('duePrice duePrice', duePrice)

    
    afterDue = customerID.due + Decimal(duePrice)
    aftertotalSpent = customerID.totalSpent + Decimal(totalPrice)

    print('afterDue afterDue', afterDue)

    Retailer.objects.filter(unique_id= customerID.unique_id).update(due=afterDue,totalSpent=aftertotalSpent)
    
    print('vvvvvvv afterDue', order)

    customerOrder = RetailerOrder()
    customerOrder.mobile_number = mobile_number
    customerOrder.address = address
    customerOrder.orderID = order
    customerOrder.retailerID = customerID
    customerOrder.save()

    # payment = RetailerPayment()
    # payment.orderID = order
    # payment.customerID = customerID
    # payment.amount = Decimal(totalPrice) - Decimal(duePrice)
    # payment.save()

    

    for productID,sellPrice,totalQty in zip(productID,sellPrice,totalQty):
        if len(productID) == 0:
            messages.warning(request, "Duplicate report add!")
            return redirect('retailer-sell-page')
        else:
            productOrder = ProductROrder()
            id = Product.objects.get(id=productID)

            afterQnty = id.stock + int(totalQty)

            productOrder.orderID = order
            productOrder.productID = id
            productOrder.sellPrice = sellPrice
            productOrder.unit = totalQty
            productOrder.save()

            Product.objects.filter(id=productID).update(stock=afterQnty)


    # return redirect('deposit-amount-order-pdf', orderId=order.id,customerId=customerID.unique_id)
    messages.error(request, "Duplicate report add!")

    return redirect('retailer-sell-page')




##########  pdf code  ###########################




class ReportLastPDF(LoginRequiredMixin, View):
    ''' This view will show lab tests pdf '''
    def get(self, request):
        orderLast = ROrder.objects.first()
        # print('orderLast')
        # print(orderLast)
        orderId = orderLast.id 
        # print(orderLast.id)
        customer = Retailer.objects.get(unique_id=orderLast.retailerID.unique_id)
        customerOrder = RetailerOrder.objects.filter(customerID=customer).first()
        # print(customerOrder)
        order = ROrder.objects.get(id=orderId)
        productOrders = ProductROrder.objects.filter(orderID=orderId)
        #reportTestinglist = ReportTestinglist.objects.filter(lab=Labreport.id)
        # tests = Labreport.report_name.all()
        #pdf = generate_pdf('admin/super/pdf/report_pdf.html', {'lab': Labreport})
        #pdf = generate_pdf('admin/super/pdf/report_pdf.html')
        
        pdf = generate_pdf('admin/super/deposit/pdf/deposit_pdf.html', {'order': order,'productOrders': productOrders,'customerOrder': customerOrder})
        return HttpResponse(pdf, content_type='application/pdf')
    

def deposit_amount_order_pdf(request,orderId,customerId):
    #pdf = generate_pdf('admin/super/pdf/report_pdf.html')

    customer = Retailer.objects.get(unique_id=customerId)
    customerOrder = RetailerOrder.objects.filter(customerID=customer).first()
    order = ROrder.objects.get(id=orderId)
    productOrders = ProductROrder.objects.filter(orderID=orderId)


    pdf = generate_pdf('admin/super/deposit/pdf/deposit_pdf.html', {'order': order,'productOrders': productOrders,'customerOrder': customerOrder})

    return HttpResponse(pdf, content_type='application/pdf')



class ReportPDF(LoginRequiredMixin, View):
    ''' This view will show lab tests pdf '''
    def get(self, request):
        Labreport = Retailer.objects.all()
        #reportTestinglist = ReportTestinglist.objects.filter(lab=Labreport.id)
        # tests = Labreport.report_name.all()
        #pdf = generate_pdf('admin/super/pdf/report_pdf.html', {'lab': Labreport})
        pdf = generate_pdf('admin/super/pdf/report_pdf.html')
        return HttpResponse(pdf, content_type='application/pdf')

