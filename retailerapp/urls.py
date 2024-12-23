from django.urls import include, path

from retailerapp.views import *
# from accounts.views import SignOutView
# from accounts.views import DoctorSignInView

# Routing Implement
urlpatterns = [ 



########     Start Customer       ########
    
    # path('add/post/', customer_add_post, name='customer-add-post'),
    path('list/', retailer_list, name='retailer-list'),
    path('add/', retailer_add, name='retailer-add'),
    path('add/post/', retailer_add_post, name='retailer-add-post'),
   
   

    
########    end  Customer       ########  


]


