

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', include('dashboard.urls')),
    path('', include('frontapp.urls')),
    path('category/', include('category.urls')),
    path('product/', include('productapp.urls')),
    path('sell/', include('sellapp.urls')),
    path('customer/', include('customerapp.urls')),
    path('deposit/', include('depositapp.urls')),
    path('return/', include('returnapp.urls')),
    path('shopapp/', include('shopapp.urls')),
    path('retailer/', include('retailerapp.urls')),
    path('retailreturnapp/', include('retailreturnapp.urls')),
]
