from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import BookingForm
from accounts.models import Staff, Customer, CustomerProfile, StaffProfile
from booking.models import Booking

from .slots import GetAllSlots, GetAllBookedSlots, CheckOverlapSlots, GenOptionTags

from datetime import time, datetime, timedelta
# Create your views here.

@login_required
def BookAppointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        print("form :::: {}".format(form))
        if form.is_valid():
            duration = form.cleaned_data['duration']
            staff = form.cleaned_data['staff']
            booking_date = form.cleaned_data['booking_date']
            start_time = (request.POST.get('start_time')).split('-')[0].strip()
            end_time = (request.POST.get('start_time')).split('-')[1].strip()
            customer = request.user.id
            print([duration,staff,booking_date,customer, start_time, end_time])


            placeholder_dt = datetime.fromisoformat(str(booking_date))
            obj_start_tm = datetime.combine(placeholder_dt, datetime.strptime(start_time, '%H:%M:%S').time()) 
            obj_end_tm = datetime.combine(placeholder_dt, datetime.strptime(end_time, '%H:%M:%S').time())
            
            staff_instance = Staff.objects.filter(pk = int(staff)).all().order_by('-pk')
            customer_instance = Customer.objects.filter(pk = int(customer)).all().order_by('-pk')

            print([duration,staff,booking_date,customer, obj_start_tm, obj_end_tm, staff_instance])
            try:
                Booking.objects.create(staff = staff_instance[0]
                                    , customer = customer_instance[0]
                                    , start_time =  obj_start_tm
                                    , end_time = obj_end_tm
                                    , durations = int(duration)
                                    , payment_status = 'Unpaid'
                                   )
                content = Booking.objects.filter(customer = customer_instance[0]).all().order_by('-pk').first()
                messages.success(request, 'Booking Submitted Successfully!!')
                return redirect('BookAppointment')
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                print(" Error while making the booking. Please try again!")
                messages.error(request, 'Booking failed. Please check the values you entered.')
                redirect('BookAppointment')
                raise
                

    else:
        form = BookingForm()
        return render(request, 'BookAppointmentPage.html', {'form':form})
    

# duration: 60
# booking_date: 2023-11-09
# staff: 19
# start_time: (datetime.time(6, 0), datetime.time(7, 0))
             

@login_required
def GetTimeslot(request):

    staff_user = request.GET.get("staff_id")
    booking_date = request.GET.get("booking_date")
    duration = request.GET.get("duration")
    # print("Content :: {}".format((staff_user, booking_date)))

    content_1 = GetAllSlots(request, staff_user, booking_date, duration)
    content_2 = GetAllBookedSlots(request, staff_user, booking_date, duration)
    AvailSlots = CheckOverlapSlots(request, content_1, content_2)

    

    AvailSlotsSTR = [["{0} - {1}".format(str(s[0]), str(s[1])), "{0} - {1}".format(str(s[0]), str(s[1])) ]for s in AvailSlots]
    final_slots_out = GenOptionTags(request, AvailSlotsSTR)
    print("AvailSlotsSTR :: {}".format(final_slots_out))
    return render(request, 'StaffTimeslots.html', {'content':final_slots_out})

    

