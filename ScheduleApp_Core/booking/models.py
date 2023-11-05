from django.db import models
from accounts.models import Staff, Customer

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='bookings_as_staff')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings_as_customer')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    durations = models.IntegerField()
    payment_status = models.CharField(max_length=20)  # Options could include 'unpaid', 'paid', 'cancelled', etc.
    
    # Add other fields specific to bookings, if needed
    # For example, you can include a 'notes' field for customer notes, 'location', 'service type', etc.

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
