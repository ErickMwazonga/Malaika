# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django imports
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView, ListView
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

# project imports
from .models import Diagnose, Room
from .forms import DiagnoseForm, RoomForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'hospital/index.html'


# create fbv for a diagnose modal form for create, update and delete
def save_diagnose_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            diagnoses = Diagnose.objects.all()
            data['html_diagnose_list'] = render_to_string("hospital/includes/partial_diagnose_list.html",
                {'diagnoses': diagnoses}
            )
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def diagnose_create(request):
    if request.method == 'POST':
        form = DiagnoseForm(request.POST)
    else:
        form = DiagnoseForm()
    return save_diagnose_form(request, form, 'hospital/diagnose_form.html')


def diagnose_update(request, pk):
    diagnose = get_object_or_404(Diagnose, pk=pk)
    if request.method == 'POST':
        form = DiagnoseForm(request.POST, instance=diagnose)
    else:
        form = DiagnoseForm(instance=diagnose)
    return save_diagnose_form(request, form, 'hospital/diagnose_update.html')


def diagnose_delete(request, pk):
    diagnose = get_object_or_404(Diagnose, pk=pk)
    data = dict()
    if request.method == 'POST':
        diagnose.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        diagnoses = Diagnose.objects.all()
        data['html_diagnose_list'] = render_to_string('hospital/includes/partial_diagnose_list.html',
            {'diagnoses': diagnoses}
        )
    else:
        context = {'diagnose': diagnose}
        data['html_form'] = render_to_string('hospital/diagnose_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

# create fbv for a room modal form for create, update and delete
def save_room_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            rooms = Room.objects.all().order_by('room_number')
            data['html_room_list'] = render_to_string('hospital/includes/partial_room_list.html',
                {'rooms': rooms}
            )
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
    else:
        form = RoomForm()
    return save_room_form(request, form, 'hospital/room_form.html')


def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
    else:
        form = RoomForm(instance=room)
    return save_room_form(request, form, 'hospital/room_update.html')


def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    data = dict()
    if request.method == 'POST':
        room.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        rooms = Room.objects.all().order_by('room_number')
        data['html_room_list'] = render_to_string('hospital/includes/partial_room_list.html',
            {'rooms': rooms}
        )
    else:
        context = {'room': room}
        data['html_form'] = render_to_string('hospital/room_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)




# cbv listviews for malaika app
class DiagnoseListView(LoginRequiredMixin, ListView):
    context_object_name = 'diagnoses'
    model = Diagnose
    template_name = 'hospital/diagnose_list.html'

    def get_queryset(self):
        return Diagnose.objects.all()


class RoomListView(LoginRequiredMixin, ListView):
    context_object_name = 'rooms'
    model = Room
    template_name = 'hospital/room_list.html'

    def get_queryset(self):
        return Room.objects.all().order_by('room_number')
