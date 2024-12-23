from django.shortcuts import render,redirect
from category.models import ProductCategory,ProductUnit
from django.contrib import messages

# Create your views here.


########     Start Category       ########



def category_add(request):
    return render(request, 'admin/super/category/add.html')

def category_add_post(request):
    name =  request.POST['name']

    productCategory = ProductCategory()
    productCategory.name = name
    productCategory.save()

    messages.success(request, "Category add successfully.")

    return redirect('category-list')

def category_list(request):

    productCategory = ProductCategory.objects.all()
    data ={
        'productCategory':productCategory
    }

    return render(request, 'admin/super/category/list.html',data)


def category_edit(request,id):

    productCategory = ProductCategory.objects.get(id=id)

    data ={
        'productCategory':productCategory
    }

    return render(request, 'admin/super/category/edit.html',data)


def category_update(request,id):
    name =  request.POST['name']
    ProductCategory.objects.filter(id=id).update(name=name)
    messages.success(request, "Category update successfully.")
    return redirect('category-list')


def category_delete(request,id):

    productCategory = ProductCategory.objects.filter(id=id)
    productCategory.delete()
    messages.success(request, "Category delete successfully.")
    return redirect('category-list')



########    end  Category       ########   




########    start  unit       ########   

def unit_add(request):
    return render(request, 'admin/super/unit/add.html')

def unit_add_post(request):
    name =  request.POST['name']

    productUnit = ProductUnit()
    productUnit.name = name
    productUnit.save()

    messages.success(request, "Unit add successfully.")

    return redirect('unit-list')

def unit_list(request):

    productUnit = ProductUnit.objects.all()
    data ={
        'productUnit':productUnit
    }

    return render(request, 'admin/super/unit/list.html',data)


def unit_edit(request,id):

    productUnit = ProductUnit.objects.get(id=id)

    data ={
        'productUnit':productUnit
    }

    return render(request, 'admin/super/unit/edit.html',data)


def unit_update(request,id):
    name =  request.POST['name']
    ProductUnit.objects.filter(id=id).update(name=name)
    messages.success(request, "Unit update successfully.")
    return redirect('unit-list')


def unit_delete(request,id):

    productUnit = ProductUnit.objects.filter(id=id)
    productUnit.delete()
    messages.success(request, "Unit delete successfully.")
    return redirect('unit-list')




########    end  unit       ########   