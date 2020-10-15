from . import views
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path

from appprincipal.registration.views import *


app_name = 'registration'



urlpatterns = [
    

    path('logout/', views.logoutUser, name = "logout"),
    path('login/', views.loginPage, name = "login"),
    path('register/', views.registerPage, name = "register"),
    


]