# flake8: noqa
# Basic Lib Import

from django.urls import include, path

from category.views import *
# from accounts.views import SignOutView
# from accounts.views import DoctorSignInView

# Routing Implement
urlpatterns = [ 


########     Start Category       ########
    
    path('category/add/', category_add, name='category-add'),
    path('category/add/post/', category_add_post, name='category-add-post'),
    path('category/list/', category_list, name='category-list'),

    path('category/edit/<int:id>', category_edit, name='category-edit'),
    path('category/update/<int:id>', category_update, name='category-update'),

    path('category/delete/<int:id>', category_delete, name='category-delete'),

    
########    end  Category       ########  


########     Start unit       ########
    
    path('unit/add/', unit_add, name='unit-add'),
    path('unit/add/post/', unit_add_post, name='unit-add-post'),
    path('unit/list/', unit_list, name='unit-list'),

    path('unit/edit/<int:id>', unit_edit, name='unit-edit'),
    path('unit/update/<int:id>', unit_update, name='unit-update'),

    path('unit/delete/<int:id>', unit_delete, name='unit-delete'),

    
########    end  unit       ########  


]


