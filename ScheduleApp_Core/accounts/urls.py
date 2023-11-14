from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.HomePage, name = 'Home' ),
    path('CustomerSignUp/', views.CustomerSignUp, name='CustomerSignUp'),
    path('StaffSignUp/', views.StaffSignUp, name='StaffSignUp'),
    path('AdminSignUp/', views.AdminSignUp, name='AdminSignUp'),

    path('login/', views.LoginView, name = 'Login'),
    path('logout/', views.LogoutView, name = 'Logout'),
]
