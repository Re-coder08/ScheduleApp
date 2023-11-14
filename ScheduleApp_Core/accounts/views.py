from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.hashers import make_password


from .models import Staff, Customer, User
from .forms import StaffSignUpForm, CustomerSignUpForm, AdminSignUpForm, LoginForm
# Create your views here.

# def HomePage(request):
#     return render(request, 'base.html')

def StaffSignUp(request):
    if request.method == 'POST':
        print("Form Submitted !!")
        form = StaffSignUpForm(request.POST)
        print("Form ::: {}".format(form))
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password1'])
            
            Staff.objects.create(username = username, password=password, email=email, is_staff = True)
            messages.success(request, 'Satff account created successfully. Please login now')
            # return render(request, 'SignUpPageStatus.html', {'signupatatus':"Success"})
            return redirect('Login')
        else:
            messages.success(request, 'Failed to Create the Staff account. Please try again')
            # return render(request, 'SignUpPageStatus.html', {'signupatatus':"Fail"})
            return redirect('StaffSignUp')
    else:
        if request.user.is_authenticated:
            logout(request)
            redirect('StaffSignUp')
        formType = 'Staff'
        form = StaffSignUpForm()

        return render(request, 'CustomSignUpPage.html', {'form': form, 'formType': formType})
    

def CustomerSignUp(request):
    if request.method == 'POST':
        print("Form Submitted !!")
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password1'])
            
            Customer.objects.create(username = username, password=password, email=email)

            # return render(request, 'SignUpPageStatus.html', {'signupatatus':"Success"})
            messages.success(request, 'Customer account created successfully. Please login now')
            return redirect('Login')
        else:
            # return render(request, 'SignUpPageStatus.html', {'signupatatus':"Fail"})
            messages.success(request, 'Failed to Create the Customer account. Please try again')
            return redirect('StaffSignUp')
    else:
        if request.user.is_authenticated:
            logout(request)
            redirect('CustomerSignUp')
        formType = 'Customer'
        form = CustomerSignUpForm()

        return render(request, 'CustomSignUpPage.html', {'form': form, 'formType': formType})


def AdminSignUp(request):
    if request.method == 'POST':
        print("Form Submitted !!")
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password1'])
            
            User.objects.create(username = username, password=password, email=email, is_staff= True, is_superuser=True)

            return render(request, 'SignUpPageStatus.html', {'signupatatus':"Success"})
        else:
            return render(request, 'SignUpPageStatus.html', {'signupatatus':"Fail"})
    else:
        formType = 'Admin'
        form = AdminSignUpForm()

        return render(request, 'CustomSignUpPage.html', {'form': form, 'formType': formType})
    


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print("user and password : {}".format((username, password)) )
            user = authenticate(request, username=username, password=password)
            print("user ::: {}".format(user))
            if user is not None:
                login(request, user)
                print("User Logged in !!")
                return redirect('Home')

            else: 
                print("Auth failed")
                return redirect('Login')


    else:
        form = LoginForm()
        return render(request, 'LoginPage.html', {'form':form})
    

def LogoutView(request):
    logout(request)
    return redirect('Home')