
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [

    path('registration/',views.user_registration, name="registration"),
    path('login/',views.user_login, name="login_page"),
    path('profile/',views.user_profile, name="profile_page"),
    path('logout/',views.user_logout, name="logout"),
    path('about_us/',TemplateView.as_view(template_name='about_us.html'), name="about_us"),
    

]
