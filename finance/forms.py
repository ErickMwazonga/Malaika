from django.forms import forms
from finance.models import Billing

class BillingForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Billing
        fields = ['pateint', 'treatment', 'charges']

    def __init__(self, *args, **kwargs):
        super(BillingForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(BillingForm, self).clean()
        return cleaned_data
