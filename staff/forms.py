from django import forms
from staff.models import Doctor

# crispy_forms imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, MultiWidgetField, Submit

class DoctorForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'gender', 'dob', 'age', 'country', 'city', 'address', 'specialization']

        labels = {
            'dob': 'Date of Birth'
        }

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'gender',
            MultiWidgetField(
                'dob',
                attrs=(
                    {'style': 'width: 30%; display: inline-block;'}
                )
            ),
            'age',
            'country',
            'city',
            'address',
            'specialization'
        )

    def clean(self):
        cleaned_data = super(DoctorForm, self).clean()
        return cleaned_data
