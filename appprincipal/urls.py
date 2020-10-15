#from core.views import LocaisList, IndexTemplateView, LocalDetailView, RegCreateView, Pt1CreateView
from . import views
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import path
from appprincipal.views import *
from . import views

app_name = 'appprincipal'

urlpatterns = [
    
    path('', IndexTemplateView.as_view(), name = 'index'),
    path('about/', AboutView.as_view(), name = "about"),
    path('termo_cond/', TermoView.as_view(), name="termo_cond"),
    path('pol/', PolView.as_view(), name="pol"),
    path('cont/', ContView.as_view(), name="cont"),


]