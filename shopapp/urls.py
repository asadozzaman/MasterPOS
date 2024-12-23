from django.urls import include, path
from shopapp.views import *
from shopapp.retailer_views import *
from shopapp.depositapp_views import *


# Routing Implement
urlpatterns = [ 

########     Start Retailer       ########
    
    # path('add/post/', customer_add_post, name='customer-add-post'),
    path('add/post/sell/', retailer_add_post_sell, name='retailer-add-post-sell'),
    path('list/', retailer_list, name='retailer-list'),
    path('add/', retailer_add, name='retailer-add'),
    path('add/post/', retailer_add_post, name='retailer-add-post'),

    
########    end  Retailer       ########  


########     Start sell       ########
    
    path('page/', sell_page, name='retailer-sell-page'),
    path('ajax/product/get/', sell_ajax_product_get, name='retailer-sell-ajax-product-get'),
    path('ajax/product/add/', sell_ajax_product_add, name='retailer-sell-ajax-product-add'),
    path('ajax/customer/info/', sell_ajax_customer_info, name='retailer-sell-ajax-customer-info'),
    path('ajax/add/post/', sell_add_post, name='retailer-sell-add-post'),
   
    path('lab-report-pdf/', ReportPDF.as_view(), name='retailer-generate_pdf'),
    path('lab-report-pdf/last/', ReportLastPDF.as_view(), name='retailer-generate_pdf-last'),
    # path('pdf/', generate_pdf, name='generate_pdf'),

    
########    end  sell       ########  



########     Start depositapp       ########
    
    path('deposit/amount/order/pdf/<int:orderId>/<str:customerId>', deposit_amount_order_pdf, name='retailer-deposit-amount-order-pdf'),
    path('deposit/amount/post/', deposit_amount_post, name='retailer-deposit-amount-post'),
    path('deposit/amount/order/post/', deposit_amount_order_post, name='retailer-deposit-amount-order-post'),
    path('deposit/filter/deposit/', deposit_filter_deposit, name='retailer-order-filter-deposit'),
    path('order/list/', deposit_order_list, name='retailer-deposit-order-list'),
    path('customer/list/', deposit_customer_list, name='retailer-deposit-customer-list'),
    path('customer/payment/history/', deposit_payment_history, name='retailer-payment-history'),
    path('customer/detail/<str:id>', deposit_customer_detail, name='retailer-deposit-customer-detail'),
 
########    end  depositapp       ########  





]


