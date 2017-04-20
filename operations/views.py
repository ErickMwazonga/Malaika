# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView, ListView
from .forms import TreatmentForm
from .models import Treatment

# create fbv for a treatment modal form for create, update and delete
def save_treatment_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            treatments = Treatment.objects.all()
            data['html_treatment_list'] = render_to_string("operations/includes/partial_treatment_list.html",
                {'treatments': treatments}
            )
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def treatment_create(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
    else:
        form = TreatmentForm()
    return save_treatment_form(request, form, 'operations/treatment_form.html')


def treatment_update(request, pk):
    treatment = get_object_or_404(Treatment, pk=pk)
    if request.method == 'POST':
        form = TreatmentForm(request.POST, instance=treatment)
    else:
        form = TreatmentForm(instance=treatment)
    return save_treatment_form(request, form, 'operations/treatment_update.html')


def treatment_delete(request, pk):
    treatment = get_object_or_404(Treatment, pk=pk)
    data = dict()
    if request.method == 'POST':
        treatment.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        treatments = Treatment.objects.all()
        data['html_treatment_list'] = render_to_string('operations/includes/partial_treatment_list.html',
            {'treatments': treatments}
        )
    else:
        context = {'treatment': treatment}
        data['html_form'] = render_to_string('operations/treatment_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)


class TreatmentListView(ListView):
    context_object_name = 'treatments'
    model = Treatment
    template_name = 'operations/treatment_list.html'

    def get_queryset(self):
        return Treatment.objects.all()
