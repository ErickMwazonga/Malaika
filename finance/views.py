# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import reverse
from django.views.generic import CreateView, ListView
from finance.models import Billing
from finance.forms import BillingForm
from django.contrib.messages.views import SuccessMessageMixin

from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

# create fbv for a billing modal form for create, update and delete
def save_billing_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            billings = Billing.objects.all()
            data['html_billing_list'] = render_to_string("finance/includes/partial_billing_list.html",
                {'billings': billings}
            )
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def billing_create(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
    else:
        form = BillingForm()
    return save_billing_form(request, form, 'finance/billing_form.html')


def billing_update(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=billing)
    else:
        form = BillingForm(instance=billing)
    return save_billing_form(request, form, 'finance/billing_update.html')


def billing_delete(request, pk):
    billing = get_object_or_404(Billing, pk=pk)
    data = dict()
    if request.method == 'POST':
        billing.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        billings = Billing.objects.all()
        data['html_billing_list'] = render_to_string('finance/includes/partial_billing_list.html',
            {'billings': billings}
        )
    else:
        context = {'billing': billing}
        data['html_form'] = render_to_string('finance/billing_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)


# Create listviews for the finance app
class BillingListView(ListView):
    context_object_name = 'billings'
    model = Billing
    template_name = 'finance/billing_list.html'

    def get_queryset(self):
        return Billing.objects.all()
