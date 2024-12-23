# flake8: noqa
# Basic Lib Import

from django.urls import include, path

from dashboard.views import *
# from accounts.views import SignOutView
# from accounts.views import DoctorSignInView

# Routing Implement
urlpatterns = [
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/filter/', admin_dashboard_filter, name='admin_dashboard_filter'),


    #all order List

    path('all/order/list/filter/', all_order_list_filter, name='all-order-list-filter'),
    path('all/order/list/', all_order_list, name='all-order-list'),
    path('all/order/detail/<str:id>',all_order_detail, name='all-order-detail'),

    # path('all/order/list/filter/retailer/', all_order_list_filter_retailer, name='all-order-list-filter-retailer'),
    path('all/order/list/retailer/', all_order_list_retailer, name='retailer-all-order-list-retailer'),
    path('all/order/detail/retailer/<str:id>',all_order_detail_retailer, name='all-order-detail-retailer'),


    # profile
    path('profile/', profile, name='profile'),
    path('profile/change/password/', profile_change_password, name='profile_change_password'),
    path('profile/change/password/post/', profile_change_password_post, name='profile_change_password_post'),
]


