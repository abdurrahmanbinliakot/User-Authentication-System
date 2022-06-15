

from django.shortcuts import render,redirect
from django.views import View
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_registration(request):
    if request.user.is_authenticated:
        return redirect('profile_page')    
    form = RegistrationForm()
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("Valid User Creation")
            form.save()
            messages.success(request, f"hey {form.cleaned_data.get('username')}, User Create Successfuly!")
            return redirect('login_page')

    return render(request,'registration.html',{"registration_form":form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile_page')  
    if request.method=="POST":
        username_ = request.POST.get('username')
        password_ = request.POST.get('password')
        user=authenticate(request,username=username_,password=password_)
        if user is not None:
            login(request,user)
            return redirect('profile_page')
        else:
            messages.info(request,'Username or Password Incorect')

    return render(request,'login_page.html',{})


@login_required(login_url='login_page')
def user_profile(request):
    return render(request,'profile_page.html',{})

def user_logout(request):
    logout(request)
    return redirect('login_page')