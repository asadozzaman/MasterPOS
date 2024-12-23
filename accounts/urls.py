# flake8: noqa
# Basic Lib Import

from django.urls import include, path

from accounts.views import SignInView
from accounts.views import SignOutView
# from accounts.views import DoctorSignInView

# Routing Implement
urlpatterns = [
    path('sign-in/', SignInView, name='sign-in'),
    # path('doctor/portal/sign-in/', DoctorSignInView, name='doctor-sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    
    # path('doctordashboard/', DcotorDashboard.as_view(), name='doctordashboard'),
]


