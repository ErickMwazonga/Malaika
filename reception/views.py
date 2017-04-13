# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView, ListView

from reception.models import Patient, In_patient, Out_patient, Diagnose
from reception.forms import PatientForm, In_patientForm, Out_patientForm

# Create your views here.
class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'reception/patient_form.html'


class In_patientCreateView(CreateView):
    model = In_patient
    template_name = 'reception/in_patient_form.html'
    form_class = In_patientForm

    def get_success_url(self):
        return render('malaika:index')


class Out_patientCreateView(CreateView):
    model = Out_patient
    template_name = 'reception/out_patient_form.html'
    form_class = Out_patientForm

    def get_success_url(self):
        return render('malaika:index')


class PatientListView(ListView):
    context_object_name = 'patient_list'
    model = Patient
    template_name = 'reception/patient_list.html'

    def get_queryset(self):
        return Patient.objects.all()


class In_patientListView(ListView):
    context_object_name = 'in_patient_list'
    model = In_patient
    template_name = 'reception/in_patient_list.html'

    def get_queryset(self):
        return In_patient.objects.all()


class Out_patientListView(ListView):
    context_object_name = 'out_patient_list'
    model = Out_patient
    template_name = 'reception/out_patient_list.html'

    def get_queryset(self):
        return Out_patient.objects.all()
