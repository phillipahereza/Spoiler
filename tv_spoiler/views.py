from django.shortcuts import render
from django.views.generic import FormView, TemplateView

# Create your views here.

class HomeView(TemplateView):
    pass


class SpoilView(FormView):
    pass


class AddVictimView(FormView):
    pass
