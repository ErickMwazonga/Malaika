# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# project imports
from django.views.generic import TemplateView
from .models import Patient, Doctor, Diagnose, Room, In_patient, Out_patient, Treatment, Billing


class IndexView(TemplateView):
    template_name = 'malaika/base.html'
