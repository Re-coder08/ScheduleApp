from django.contrib import admin
from .models import User, Staff, StaffProfile, StaffManager, Customer, CustomerProfile, CustomerManager

from django.contrib.auth.models import Group, Permission
# Register your models here.





class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role',)
    search_fields = ('username', 'role',)
    filter_horizontal = ('groups', 'user_permissions',)



admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(CustomerProfile)
admin.site.register(Staff)
admin.site.register(StaffProfile)


# admin.site.register(Permission)
