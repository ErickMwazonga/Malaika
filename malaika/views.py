# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse

# project imports
from django.views.generic import TemplateView, CreateView, ListView
from .models import Diagnose, Room
from .forms import DiagnoseForm, RoomForm
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(TemplateView):
    template_name = 'malaika/index.html'


# creating objects of the models using CBV CreateView
class DiagnoseCreateView(SuccessMessageMixin, CreateView):
    model = Diagnose
    template_name = 'malaika/diagnose_form.html'
    form_class = DiagnoseForm
    success_message = 'Diagnose entered successfully'

    def get_success_url(self):
        return reverse('malaika:index')


class RoomCreateView(SuccessMessageMixin, CreateView):
    model = Room
    template_name = 'malaika/room_form.html'
    form_class = RoomForm
    success_message = 'Room entered successfully'

    def get_success_url(self):
        return reverse('')

# cbv listviews for malaika app
class DiagnoseListView(ListView):
    context_object_name = 'diagnose_list'
    model = Diagnose
    template_name = 'TEMPLATE_NAME'

    def get_queryset(self):
        return Diagnose.objects.all()


class RoomListView(ListView):
    context_object_name = 'rooms_list'
    model = Room
    template_name = 'TEMPLATE_NAME'

    def get_queryset(self):
        return Room.objects.all()
