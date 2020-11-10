from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
from solicitudes.models import Solicitud
from django.views import generic
from django.urls import reverse_lazy 
from solicitudes.forms import SolicitudForm


class HomePageView(generic.CreateView):
    model = Solicitud
    template_name = 'index.html'
    form_class = SolicitudForm
    context_object_name = 'context'    
    success_url = reverse_lazy("home")
    success_message=("Solicitud Creada Satisfactoriamente")



