# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Doctor
from .forms import DoctorForm

# Create your views here.
class DoctorCreateView(SuccessMessageMixin, CreateView):
    model = Doctor
    template_name = 'staff/doctor_form.html'
    form_class = DoctorForm
    success_message = "Doctor's details entered successfully"

    def get_success_url(self):
        return reverse('malaika:index')


class DoctorListView(ListView):
    context_object_name = 'doctors_list'
    model = Doctor
    template_name = 'TEMPLATE_NAME'

    def get_queryset(self):
        return Doctor.objects.all()
