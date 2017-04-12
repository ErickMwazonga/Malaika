# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView
from staff.models import Doctor

# Create your views here.
class DoctorCreateView(CreateView):
    model = Doctor
    template_name = ''
    form_class = ''
