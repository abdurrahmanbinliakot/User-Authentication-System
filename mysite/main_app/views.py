
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect
from django.views import View
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, admin_only

# Create your views here.

def user_registration(request):
    if request.user.is_authenticated:
        return redirect('index_page')    
    form = RegistrationForm()
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("Valid User Creation")
            user =form.save()
            group_=Group.objects.get(name='customar')
            user.groups.add(group_)
            messages.success(request, f"hey {form.cleaned_data.get('username')}, User Create Successfuly!")
            return redirect('login_page')

    return render(request,'registration.html',{"registration_form":form})

@unauthenticated_user
def user_login(request):

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
    if request.method == "GET":
        # form = RegistrationForm(instance=request.user)
        # form = RegistrationForm(instance={'username':'hasan'})
        return render(request,'profile_page.html',{})

@login_required(login_url='login_page')
def user_logout(request):
    logout(request)
    return redirect('login_page')