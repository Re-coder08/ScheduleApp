from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.models import Customer
from .forms import MyAccountForm

# Create your views here.
def HomePage(request):
    if request.method == 'POST':
        pass
    else:
        if request.user.is_authenticated:
            content = request.user.username
            return render(request, 'Home.html', {'content':content})
        else:
            return redirect('Login')

@login_required
def MyClasses(request):
    if request.method == 'POST':
        pass
    else:
        content = "My Classes"
        return render(request, 'Myclasses.html', {'content': content})
    
@login_required
def MyAccount(request):

    if request.method == "GET":
    
        user_data = Customer.objects.filter(pk = request.user.id).order_by('-pk').all().values_list('username', 'first_name', 'last_name', 'email')[0]
        # user_data = get_object_or_404(Customer, pk=request.user.id)
        print(f'test :: {user_data}')
        content = {'username': user_data[0]
                   ,'first_name': user_data[1]
                    ,'last_name':user_data[2]
                     ,'email':user_data[3] }
        return render(request, 'Myaccount.html', content)
        # queryset = YourModel.objects.all()
        

@login_required
def MyAccountEdit(request):

    if request.method == 'POST':
        form = MyAccountForm(request.POST)
        print(f'form data ::: {form}')
        # if form.is_valid():
        ## add validatin here befor updating the values in the database
        
        # username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email'] 

        print(f'the form data ::: {[first_name, last_name, email]}')

        # check if there is any change to the values beofre updatong the record in db.
        try:
            Customer.objects.filter(pk=request.user.id).update(first_name = first_name, last_name = last_name, email = email)
            print(f'Updated the Customer values Successfully to : {[ first_name, last_name, email]}')
            messages.error(request, 'Profile updated Successfully.')
            return redirect('MyAccount')
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            print(" Error while making the booking. Please try again!")
            messages.error(request, 'Profile update Failed. Please check the values you entered.')
            redirect('BookAppointment')
            raise 
            

    if request.method == 'GET':
        user_data = Customer.objects.filter(pk = request.user.id).order_by('-pk').all()[0]
        form = MyAccountForm(instance=user_data)
        content = { 'form': form}
        return render(request, 'Myaccountedit.html', content)




        