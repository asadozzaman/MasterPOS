from django.urls import include, path

from customerapp.views import *
# from accounts.views import SignOutView
# from accounts.views import DoctorSignInView

# Routing Implement
urlpatterns = [ 



########     Start Customer       ########
    
    # path('add/post/', customer_add_post, name='customer-add-post'),
    path('add/post/sell/', customer_add_post_sell, name='customer-add-post-sell'),
    path('list/', customer_list, name='customer-list'),
    path('add/', customer_add, name='customer-add'),
    path('add/post/', customer_add_post, name='customer-add-post'),
   
   

    
########    end  Customer       ########  


]


