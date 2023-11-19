from django.contrib import admin

from .models import Booking



class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'staff', 'customer','durations', 'payment_status',)
    search_fields = ('booking_id', 'staff', 'customer','durations', 'payment_status',)

# Register your models here.
admin.site.register(Booking, BookingAdmin)