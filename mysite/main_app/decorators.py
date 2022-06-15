from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages


def unauthenticated_user(view_fuc):
    def wraper_fuc(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile_page')
        else:
            return view_fuc(request,*args, **kwargs)
    return wraper_fuc

def admin_only(view_func):
    def admin_wrapper_func(request,*args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'seller':
            messages.warning(request,'You are not an Admin')
            return redirect('orders')
        if group == 'worker':
            return redirect('checkout')
        if group == 'customar':
            messages.warning(request,'You are not an Admin')
            return redirect('checkout')
        if group == 'admin':
            return view_func(request,*args, **kwargs)
    return admin_wrapper_func

def allowed_users(user_list=[]):
    def allowed_func(view_func):
        def wrapper_func(request,*args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in user_list:
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse("You are Not Athorized to view is page")

        return wrapper_func
    return allowed_func
