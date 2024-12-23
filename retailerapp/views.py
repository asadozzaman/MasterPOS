from shopapp.models import Retailer
from django.shortcuts import render,redirect
from django.contrib import messages
from accounts.unique_uuid import unique_code
from accounts.models import User

# Create your views here.


def retailer_list(request):

    customer = Retailer.objects.all()
    
    data={
        'customer' : customer
    }
    

    return render(request, 'admin/super/retailer/list.html',data)


def retailer_add(request):

    return render(request, 'admin/super/retailer/add.html')



def retailer_add_post(request):
    name =  request.POST['name']
    mobile_number =  request.POST['mobile_number']
    address =  request.POST['address']

    user = User()
    user.first_name = name
    user.username = mobile_number
    user.address = address
    user.mobile_number = mobile_number
    user.save()

    customer = Retailer()
    customer.unique_id = f'{unique_code(10)}'
    customer.user = user
    customer.save()

    messages.success(request, "Retailer add successfully.")

    return redirect('retailer-list')

