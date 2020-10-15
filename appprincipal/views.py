from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, JsonResponse
from appprincipal.registration.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views
from django.contrib.auth.decorators import login_required #para Functions Based Views
from django.contrib.auth.forms import UserCreationForm #formulario Users
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from appprincipal.registration.forms import *
from django.views.generic.edit import UpdateView 
from django.contrib import messages
from appprincipal.registration.decorators import unauthenticated_user, allowed_users, admin_only
import json
import datetime




# Create your views here.

class IndexTemplateView(TemplateView):
    template_name = "index.html"
    @method_decorator(login_required, allowed_users(allowed_roles=['customer']))
    def get (self, request):
        return render(request, self.template_name)

class AboutView(View):
    template = "about.html"
    @method_decorator(login_required, admin_only)
    def get (self, request):

        return render(request, self.template)

class TermoView(View):
    template = "termo.html"
    def get (self, request):

        return render(request, self.template)

class PolView(View):
    template = "pol.html"
    def get (self, request):

        return render(request, self.template)

class ContView(View):
    template = "cont.html"
    def get (self, request):

        return render(request, self.template)
