from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import BookingForm
# Create your views here.

@login_required
def BookAppointment(request):

    form = BookingForm()
    return render(request, 'BookAppointmentPage.html', {'form':form})

@login_required
def GetTimeslot(request):

    content = request.GET.get("staff")
    print("Content :: {}".format(content))

    return render(request, 'StaffTimeslots.html', {'content':content})