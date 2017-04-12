# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView
from reception.nodels import Patient, In_patient, Out_patient, Diagnose

# Create your views here.
class PatientCreateView(CreateView):
    model = Patient
    template_name = ''
    form_class = ''

    def get_success_url(self):
        return render('')


class In_patientCreateView(CreateView):
    model = In_patient
    template_name = ''
    form_class = ''

    def get_success_url(self):
        return render('')


class Out_patientCreateView(CreateView):
    model = Out_patient
    template_name = ''
    form_class = ''

    def get_success_url(self):
        return render('')
