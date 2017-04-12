# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView
from finance.models import Billing

# Create your views here.
class BillingCreateView(CreateView):
    model = Billing
    template_name = ''
    form_class = ''

    def get_success_url(self):
        return render('')
