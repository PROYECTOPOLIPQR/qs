from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings

class IndexView(TemplateView):
    template_name = 'index.html'

class HomePageView(TemplateView):
    template_name = "index.html"



