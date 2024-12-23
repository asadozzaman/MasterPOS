from accounts.models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import View


# Create your views here.

def SignInView(request):
    if request.method == 'POST':
        email = request.POST['email']
        # username = request.POST['username']
        password = request.POST['login[password]']

        print('gggggggg')
        print('password',password)

        try:
            user = User.objects.get(email = email)
                    
            if user.check_password(password) :
                login(request, user)
                if user.is_sub:
                    return redirect('admin_dashboard')
                elif user.is_customer:
                    return redirect('admin_dashboard')
                elif user.is_superuser:
                    return redirect('admin_dashboard')
                else:
                    return render(request, 'admin/login.html')
                
            
        except User.DoesNotExist:
            return render(request, 'admin/login.html')
        
        # print('my mobile_number',mobile_number)
        # # user = auth.authenticate(mobile_number=mobile_number, password=password)
        # user = User.objects.get(mobile_number = mobile_number)
       
        # print('my value',user)
        
        # if user.check_password(password) :
        #     login(request, user)
        #     return redirect("dashboard")

        # print('my value',user)
        # if user is not None:
        #     auth.login(request, user)
        #     # messages.success(request, 'Login Successfull')
        #     # return redirect('dashboard')
        #     if user.is_sub:
        #         return redirect('dashboard')
        #     elif user.is_doctor:
        #         return redirect('doctordashboard')
        #     elif user.is_superuser:
        #         return redirect('dashboard')
        #     else:
        #         return redirect('dashboard')
        #     url = request.META.get('HTTP_REFERER')
        # else:
        #     # messages.error(request, 'Invalid login crisidals')
        #     return redirect('sign-in')
    return render(request, 'admin/login.html')


class SignOutView(LoginRequiredMixin, View):
    ''' Logoutview will logout the current login user '''

    def get(self, request):
        logout(request)
        return redirect('/')
