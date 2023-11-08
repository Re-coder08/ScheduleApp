from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import BookingForm
from accounts.models import Staff, Customer, CustomerProfile, StaffProfile
from booking.models import Booking

from datetime import time, datetime, timedelta
# Create your views here.

@login_required
def BookAppointment(request):

    form = BookingForm()
    return render(request, 'BookAppointmentPage.html', {'form':form})


def add_duration_to_date(request, start_tm, add_dur):
    print("add duration data  ::: {0},, {1}".format(start_tm, add_dur))
    placeholder_dt = datetime.fromisoformat('9999-01-01')
    append_tm = datetime.combine(placeholder_dt, start_tm[0]) + timedelta(hours=add_dur.hour, minutes=add_dur.minute)
    print("after time  ::: {0},, {1}".format(start_tm, append_tm))
    
    return (append_tm.time(), )  

def GetAllSlots(request, staff_id, booking_date, duration):
        
        start_tm = StaffProfile.objects.filter(user_id = int(staff_id)).all().values_list('staff_start_time')[0]
        end_tm = StaffProfile.objects.filter(user_id = int(staff_id)).all().values_list('staff_end_time')[0]
        # print("All data : {}".format((request, staff_id, start_tm[0], str(start_tm[0]), str(end_tm[0]))))

        slots = [start_tm]
        add_dur = duration
        if duration == '60':
            add_dur = time.fromisoformat('01:00:00')
        if duration == '30' or duration == None:
            add_dur = time.fromisoformat('00:30:00')

        while start_tm[0] < end_tm[0]:
            start_tm = add_duration_to_date(request, start_tm, add_dur)
            # print(start_tm)
            slots.append(start_tm)

        slots = [ i[0] for i in slots]
        print("here : {}".format(slots))
        return slots

def GetAllBookedSlots(request, staff_user, booking_date, duration):
     print(type(staff_user))
     BookedSlots = Booking.objects.filter(staff_id = int(staff_user)).all().values_list('start_time', 'end_time')
     print("Booked Slots : {0} ".format(BookedSlots))

@login_required
def GetTimeslot(request):

    staff_user = request.GET.get("staff_id")
    booking_date = request.GET.get("booking_date")
    duration = request.GET.get("duration")
    # print("Content :: {}".format((staff_user, booking_date)))

    content_1 = GetAllSlots(request, staff_user, booking_date, duration)
    content_2 = GetAllBookedSlots(request, staff_user, booking_date, duration)

    return render(request, 'StaffTimeslots.html', {'content':content_1[0]})

