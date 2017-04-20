# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView

from reception.models import Patient, In_patient, Out_patient, Diagnose
from reception.forms import PatientForm, In_patientForm, Out_patientForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class PatientCreateView(SuccessMessageMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'reception/patient_form.html'
    success_message = 'Patient records entered successfully'

    def get_success_url(self):
        return reverse_lazy('reception:patients')


class In_patientCreateView(SuccessMessageMixin, CreateView):
    model = In_patient
    template_name = 'reception/in_patient_form.html'
    form_class = In_patientForm
    success_message = 'In-Patient records entered successfully'

    def get_success_url(self):
        return reverse_lazy('reception:patients')


class Out_patientCreateView(SuccessMessageMixin, CreateView):
    model = Out_patient
    template_name = 'reception/out_patient_form.html'
    form_class = Out_patientForm
    success_message = 'Out-Patient records entered successfully'

    def get_success_url(self):
        return reverse_lazy('reception:patients')


class PatientListView(ListView):
    context_object_name = 'patient_list'
    model = Patient
    template_name = 'reception/reception_list.html'

    def get_queryset(self):
        return Patient.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PatientListView, self).get_context_data(**kwargs)
        context['in_patient_list'] = In_patient.objects.all()
        context['out_patient_list'] = Out_patient.objects.all()
        return context


class In_patientListView(ListView):
    context_object_name = 'in_patient_list'
    model = In_patient
    template_name = 'reception/reception_list.html'

    def get_queryset(self):
        return In_patient.objects.all()


class Out_patientListView(ListView):
    context_object_name = 'out_patient_list'
    model = Out_patient
    template_name = 'reception/reception_list.html'

    def get_queryset(self):
        return Out_patient.objects.all()
