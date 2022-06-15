
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from django import forms


# class RegistrationForm(forms.ModelForm):
#     email = forms.EmailField(label='Confirm Email')
#     password1 = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields =['username','first_name', 'last_name', 'email','password1','password2']
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         email_qs = User.objects.filter(email=email)
#         if email_qs.exists():
#             raise forms.ValidationError("This email has already been registered")
#         return email

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','first_name', 'last_name', 'email','password1','password2']
    
    error_messages ={
        "password_mismatch": "password milsena.",
        "clean_email_error":"Onno mail diye tray koren"
    }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(self.error_messages["clean_email_error"])
        return email