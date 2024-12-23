from django.shortcuts import render,redirect
from productapp.models import Product
from django.contrib import messages
from category.models import ProductCategory,ProductUnit
from accounts.unique_uuid import unique_code


# Create your views here.



########    start  unit       ########   

def product_add(request):
    productCategory = ProductCategory.objects.all()
    productUnit = ProductUnit.objects.all()

    data ={
        'productCategory':productCategory,
        'productUnit':productUnit,
    }


    return render(request, 'admin/super/product/add.html',data)

def product_add_post(request):
    name =  request.POST['name']
    category =  request.POST['category']
    unit =  request.POST['unit']
    buyPrice =  request.POST['buyPrice']
    sellPrice =  request.POST['sellPrice']
    stock =  request.POST['stock']
    discount =  request.POST['discount']

    productUnit = ProductUnit.objects.get(id=unit)
    productCategory = ProductCategory.objects.get(id=category)

    product = Product()
    product.unique_id = f'{unique_code(10)}'
    product.name = name
    product.category = productCategory
    product.unit = productUnit
    product.buyPrice = buyPrice
    product.sellPrice = sellPrice
    product.stock = stock
    product.discount = discount
    product.save()

    messages.success(request, "Product add successfully.")

    return redirect('product-list')

def product_list(request):

    product = Product.objects.all()
    data ={
        'product':product,
    }

    return render(request, 'admin/super/product/list.html',data)


def product_edit(request,id):

    product = Product.objects.get(id=id)
    productCategory = ProductCategory.objects.all()
    productUnit = ProductUnit.objects.all()

    data ={
        'product':product,
        'productCategory':productCategory,
        'productUnit':productUnit,
    }

    return render(request, 'admin/super/product/edit.html',data)


def product_update(request,id):
    name =  request.POST['name']
    category =  request.POST['category']
    unit =  request.POST['unit']
    buyPrice =  request.POST['buyPrice']
    sellPrice =  request.POST['sellPrice']
    stock =  request.POST['stock']
    discount =  request.POST['discount']

    productUnit = ProductUnit.objects.get(id=unit)
    productCategory = ProductCategory.objects.get(id=category)
    
    Product.objects.filter(id=id).update(name=name,category=productCategory,unit=productUnit,buyPrice=buyPrice,sellPrice=sellPrice,stock=stock,discount=discount)
    messages.success(request, "Product update successfully.")
    return redirect('product-list')


def product_delete(request,id):

    product = Product.objects.filter(id=id)
    product.delete()
    messages.success(request, "Product delete successfully.")
    return redirect('product-list')




########    end  unit       ########  