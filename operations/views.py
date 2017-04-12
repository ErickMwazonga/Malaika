# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.
class TreatmentCreateView(CreateView):
    model = Treatment
    template_name = ''
    form_class = ''

    def get_success_url(self):
        return render('')
