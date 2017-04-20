# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

from .models import Doctor
from .forms import DoctorForm

# create fbv for a doctor modal form for create, update and delete
def save_doctor_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            doctors = Doctor.objects.all()
            data['html_doctor_list'] = render_to_string("staff/includes/partial_doctor_list.html",
                {'doctors': doctors}
            )
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
    else:
        form = DoctorForm()
    return save_doctor_form(request, form, 'staff/doctor_form.html')


def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
    else:
        form = DoctorForm(instance=doctor)
    return save_doctor_form(request, form, 'staff/doctor_update.html')


def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    data = dict()
    if request.method == 'POST':
        doctor.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        doctors = Doctor.objects.all()
        data['html_doctor_list'] = render_to_string('staff/includes/partial_doctor_list.html',
            {'doctors': doctors}
        )
    else:
        context = {'doctor': doctor}
        data['html_form'] = render_to_string('staff/doctor_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)


class DoctorListView(ListView):
    context_object_name = 'doctors'
    model = Doctor
    template_name = 'staff/doctor_list.html'

    def get_queryset(self):
        return Doctor.objects.all()
