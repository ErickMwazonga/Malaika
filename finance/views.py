# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView
from finance.models import Billing
from finance.forms import BillingForm

# Create your views here.
class BillingCreateView(CreateView):
    model = Billing
    template_name = 'finance/billing_form.html'
    form_class = BillingForm

    def get_success_url(self):
        return render('')
