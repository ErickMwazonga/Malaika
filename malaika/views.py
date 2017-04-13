# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# project imports
from django.views.generic import TemplateView, CreateView
from .models import Diagnose, Room
from .forms import DiagnoseForm, RoomForm


class IndexView(TemplateView):
    template_name = 'malaika/index.html'


# creating objects of the models using CBV CreateView
class DiagnoseCreateView(CreateView):
    model = Diagnose
    template_name = 'malaika/diagnose_form.html'
    form_class = DiagnoseForm

    def get_success_url(self):
        return reverse('')


class RoomCreateView(CreateView):
    model = Room
    template_name = 'malaika/room_form.html'
    form_class = RoomForm

    def get_success_url(self):
        return reverse('')
