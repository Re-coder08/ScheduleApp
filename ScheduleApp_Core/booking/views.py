from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import BookingForm
from accounts.models import Staff, Customer, CustomerProfile, StaffProfile
# Create your views here.

@login_required
def BookAppointment(request):

    form = BookingForm()
    return render(request, 'BookAppointmentPage.html', {'form':form})


def GetOpenSlots(request, staff_id, booking_date):
        start_tm = StaffProfile.objects.filter(pk = staff_id).all().values_list('staff_start_time')
        end_tm = StaffProfile.objects.filter(pk = staff_id).all().values_list('staff_end_time')
        print("All data : {}".format((request, staff_id, start_tm, end_tm)))

        # res = []

        # while start_tm >= end_tm:
        #     res.append()
        return [str(start_tm[0][0]), str(end_tm[0][0])]

@login_required
def GetTimeslot(request):

    staff_user = request.GET.get("staff_id")
    booking_date = request.GET.get("booking_date")
    print("Content :: {}".format((staff_user, booking_date)))

    content_1 = GetOpenSlots(request, staff_user, booking_date)

    return render(request, 'StaffTimeslots.html', {'content':content_1[0]})

@login_required
def GetTimeslot1(request):
    print("1: {0} and {1}". format(request.GET.get("staff_id"), request.GET.get("booking_date")))