from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomePage, name = 'Home' ),
    path('dashboard/Myclasses/', views.MyClasses, name = 'MyClasses'),
    path('dashboard/Myaccount/', views.MyAccount, name = 'MyAccount'),
    path('dashboard/Myaccount/edit/', views.MyAccountEdit, name = 'MyAccountEdit')
]
