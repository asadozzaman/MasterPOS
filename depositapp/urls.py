# flake8: noqa
# Basic Lib Import

from django.urls import include, path
from depositapp.views import *


urlpatterns = [ 

########     Start depositapp       ########
    
    path('deposit/amount/order/pdf/<int:orderId>/<str:customerId>', deposit_amount_order_pdf, name='deposit-amount-order-pdf'),
    path('deposit/amount/post/', deposit_amount_post, name='deposit-amount-post'),
    path('deposit/amount/order/post/', deposit_amount_order_post, name='deposit-amount-order-post'),
    path('deposit/filter/deposit/', deposit_filter_deposit, name='order-filter-deposit'),
    path('order/list/', deposit_order_list, name='deposit-order-list'),
    path('customer/list/', deposit_customer_list, name='deposit-customer-list'),
    path('customer/payment/history/', deposit_payment_history, name='payment-history'),
    path('customer/detail/<str:id>', deposit_customer_detail, name='deposit-customer-detail'),
 
########    end  depositapp       ########  


]


