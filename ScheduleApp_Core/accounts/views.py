from django.shortcuts import render

from .models import Staff, Customer, User
from .forms import StaffSignUpForm, CustomerSignUpForm, AdminSignUpForm
# Create your views here.

def HomePage(request):
    return render(request, 'base.html')

def StaffSignUp(request):
    if request.method == 'POST':
        print("Form Submitted !!")
        form = StaffSignUpForm(request.POST)
        print("Form ::: {}".format(form))
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            
            Staff.objects.create(username = username, password=password, email=email)

            return render(request, 'SignUpPageStatus.html', {'signupatatus':"Success"})
        else:
            return render(request, 'SignUpPageStatus.html', {'signupatatus':"Fail"})
    else:
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
            password = form.cleaned_data['password1']
            
            Customer.objects.create(username = username, password=password, email=email)

            return render(request, 'SignUpPageStatus.html', {'signupatatus':"Success"})
        else:
            return render(request, 'SignUpPageStatus.html', {'signupatatus':"Fail"})
    else:
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
            password = form.cleaned_data['password1']
            
            User.objects.create(username = username, password=password, email=email, is_staff= True, is_superuser=True)

            return render(request, 'SignUpPageStatus.html', {'signupatatus':"Success"})
        else:
            return render(request, 'SignUpPageStatus.html', {'signupatatus':"Fail"})
    else:
        formType = 'Admin'
        form = AdminSignUpForm()

        return render(request, 'CustomSignUpPage.html', {'form': form, 'formType': formType})