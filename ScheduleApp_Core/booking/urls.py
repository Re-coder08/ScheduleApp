from django.urls import path, include

from . import views

urlpatterns = [
    
    path('BookAppointment/', views.BookAppointment, name='BookAppointment'),
    path('BookAppointment/Timeslot/', views.GetTimeslot, name = 'GetTimeslot')
    # path('AddCredits/', views.StaffSignUp, name='StaffSignUp'),

]