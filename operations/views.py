# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView
from .forms import TreatmentForm
from .models import Treatment

# Create your views here.
class TreatmentCreateView(CreateView):
    model = Treatment
    template_name = 'operations/treatment_form.html'
    form_class = TreatmentForm

    def get_success_url(self):
        return reverse('malaika:index')


class TreatmentListView(ListView):
    context_object_name = 'treatment_list'
    model = Treatment
    template_name = 'TEMPLATE_NAME'

    def get_queryset(self):
        return Treatment.objects.all()
