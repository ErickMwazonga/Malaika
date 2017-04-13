# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.views.generic import CreateView, ListView
from finance.models import Billing
from finance.forms import BillingForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class BillingCreateView(SuccessMessageMixin, CreateView):
    model = Billing
    template_name = 'finance/billing_form.html'
    form_class = BillingForm
    success_message = 'Charges Recorded successfully'

    def get_success_url(self):
        return reverse('malaika:index')


# Create listviews for the finance app
class BillingListView(ListView):
    context_object_name = 'billing_list'
    model = Billing
    template_name = 'TEMPLATE_NAME'

    def get_queryset(self):
        return reverse('malaika:index')
