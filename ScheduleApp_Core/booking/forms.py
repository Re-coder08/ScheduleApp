from django import forms
from .models import Booking
from accounts.models import Staff

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.Form):
    # email = forms.EmailField(max_length=200, help_text='Required')
    duration = forms.ChoiceField(required=True, choices=[('30', '30'), ('60','60')])
    booking_date = forms.DateField(required=True, widget=DateInput) #DateInput(attrs={"hx-get":"Timeslot/", "hx-target":"#id_start_time"})
    staff = forms.ChoiceField(required=True, choices=[(i.pk, i.username) for i in Staff.objects.filter(role = 'STAFF').all()]
                            #   , widget=forms.Select(attrs={"hx-get":"Timeslot/", "hx-target":"#id_start_time"})
                              )
    start_time = forms.ChoiceField(choices=[("FA", "First Avail")])

    class Meta:
        model = Booking
        fields = ('duration','booking_date','staff','start_time')

