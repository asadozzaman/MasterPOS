# flake8: noqa
# Basic Lib Import

from django.urls import include, path

from retailreturnapp.views import *
# from accounts.views import SignOutView
# from accounts.views import DoctorSignInView

# Routing Implement
urlpatterns = [ 



########     Start product       ########
    
    path('return/list/', return_list, name='retailer-return-list'),
    path('return/detail/<str:id>',return_detail, name='retailer-return-detail'),
    path('return/post/', return_post, name='retailer-return-post'),
    path('return/filter/return/', return_filter_return, name='retailer-order-filter-return'),

    

    
########    end  product       ########  


]


