from customerapp.models import Customer
from django.shortcuts import render,redirect
from django.contrib import messages
from accounts.unique_uuid import unique_code
from accounts.models import User

# Create your views here.


def customer_list(request):

    customer = Customer.objects.all()
    
    data={
        'customer' : customer
    }
    

    return render(request, 'admin/super/customer/list.html',data)


def customer_add(request):

    return render(request, 'admin/super/customer/add.html')



def customer_add_post(request):
    name =  request.POST['name']
    mobile_number =  request.POST['mobile_number']
    address =  request.POST['address']

    user = User()
    user.first_name = name
    user.username = mobile_number
    user.address = address
    user.mobile_number = mobile_number
    user.save()

    customer = Customer()
    customer.unique_id = f'{unique_code(10)}'
    customer.user = user
    customer.save()

    messages.success(request, "Customer add successfully.")

    return redirect('customer-list')

def customer_add_post_sell(request):
    name =  request.POST['name']
    mobile_number =  request.POST['mobile_number']
    address =  request.POST['address']

    user = User()
    user.first_name = name
    user.username = mobile_number
    user.address = address
    user.mobile_number = mobile_number
    user.save()

    customer = Customer()
    customer.unique_id = f'{unique_code(10)}'
    customer.user = user
    customer.save()

    messages.success(request, "Customer add successfully.")

    return redirect('sell-page')