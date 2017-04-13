from django import forms
from finance.models import Billing

# crispy_forms imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import  Submit, Layout
from crispy_forms.bootstrap import PrependedAppendedText

class BillingForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Billing
        fields = ['patient', 'treatment', 'charges']

    def __init__(self, *args, **kwargs):
        super(BillingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

        self.helper.layout = Layout(
            'patient',
            'treatment',
            PrependedAppendedText('charges', 'Kshs.', '.00'),
        )

    def clean(self):
        cleaned_data = super(BillingForm, self).clean()
        return cleaned_data
