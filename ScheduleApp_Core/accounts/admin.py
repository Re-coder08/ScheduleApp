from django.contrib import admin
from .models import User, Staff, StaffProfile, StaffManager, Customer, CustomerProfile, CustomerManager
# Register your models here.

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(CustomerProfile)
admin.site.register(Staff)
admin.site.register(StaffProfile)