# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# project imports
from django.views.generic import TemplateView, CreateView
from malaika.models import Diagnose, Room


class IndexView(TemplateView):
    template_name = 'malaika/index.html'

# creating objects of the models using CBV CreateView

class DiagnoseCreateView(CreateView):
    model = Diagnose
    template_name = ''
    form_class = ''

    def get_success_url(self):
        return render('')


class RoomCreateView(CreateView):
    model = Room
    template_name = ''
    form_class = ''

    def get_success_url(self):
        return render('')
