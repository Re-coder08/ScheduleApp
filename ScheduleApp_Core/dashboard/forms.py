from django import forms

from accounts.models import Customer, User, Staff, CustomerProfile



class MyAccountForm(forms.ModelForm):
    
    class Meta:
            model = Customer
            fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(MyAccountForm, self).__init__(*args, **kwargs)

        # Disable a specific field (e.g., 'field2')
        self.fields['username'].disabled = True
        self.fields['email']
            



        
            
    





    
