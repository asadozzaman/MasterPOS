# flake8: noqa
# Basic Lib Import

from django.urls import include, path

from sellapp.views import *
# from accounts.views import SignOutView
# from accounts.views import DoctorSignInView

# Routing Implement
urlpatterns = [ 



########     Start sell       ########
    
    path('page/', sell_page, name='sell-page'),
    path('ajax/product/get/', sell_ajax_product_get, name='sell-ajax-product-get'),
    path('ajax/product/add/', sell_ajax_product_add, name='sell-ajax-product-add'),
    path('ajax/customer/info/', sell_ajax_customer_info, name='sell-ajax-customer-info'),
    path('ajax/add/post/', sell_add_post, name='sell-add-post'),
   
    path('lab-report-pdf/', ReportPDF.as_view(), name='generate_pdf'),
    path('lab-report-pdf/last/', ReportLastPDF.as_view(), name='generate_pdf-last'),
    # path('pdf/', generate_pdf, name='generate_pdf'),

    
########    end  sell       ########  


]


