# flake8: noqa
# Basic Lib Import

from django.urls import include, path

from productapp.views import *
# from accounts.views import SignOutView
# from accounts.views import DoctorSignInView

# Routing Implement
urlpatterns = [ 



########     Start product       ########
    
    path('product/add/', product_add, name='product-add'),
    path('product/add/post/', product_add_post, name='product-add-post'),
    path('product/list/', product_list, name='product-list'),

    path('product/edit/<int:id>', product_edit, name='product-edit'),
    path('product/update/<int:id>', product_update, name='product-update'),

    path('product/delete/<int:id>', product_delete, name='product-delete'),

    
########    end  product       ########  


]


