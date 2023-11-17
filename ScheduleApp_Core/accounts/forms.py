from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Staff, Customer, User



class StaffSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = Staff
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(StaffSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False

        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password1'})
        self.fields['password1'].label = False

        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password2'})
        self.fields['password2'].label = False

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['email'].label = False
        

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = Customer
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(CustomerSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False

        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password1'})
        self.fields['password1'].label = False

        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password2'})
        self.fields['password2'].label = False

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['email'].label = False

class AdminSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(AdminSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False

        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password1'})
        self.fields['password1'].label = False

        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password2'})
        self.fields['password2'].label = False

        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['email'].label = False

    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password'].label = False


    
