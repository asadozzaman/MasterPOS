# flake8: noqa
# Basic Lib Import

from django.urls import include, path

from frontapp.views import frontui
# from accounts.views import SignOutView
# from accounts.views import DoctorSignInView

# Routing Implement
urlpatterns = [
    path('', frontui, name='frontui'),
]


