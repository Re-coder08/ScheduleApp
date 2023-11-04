from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Staff, Customer, User

class StaffSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = Staff
        fields = ('username', 'email', 'password1', 'password2')

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = Customer
        fields = ('username', 'email', 'password1', 'password2')

class AdminSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')
