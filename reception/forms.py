from django.forms import forms
from reception.models import Patient, In_patient, Out_patient

# crispy_forms imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, MultiWidgetField, Submit


class PatientForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'dob', 'age', 'country', 'city', 'address', 'contact_no', 'next_of_kin']

        labels = {
            'dob': 'Date of Birth',
            'contact_no': 'Contact Number'
        }

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
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
            'contact_no',
            'next_of_kin',
        )

    def clean(self):
        cleaned_data = super(PatientForm, self).clean()
        return cleaned_data


class In_patientForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = In_patient
        fields = ['patient', 'date_of_adm', 'date_of_discarge', 'diagnosis', 'doctor', 'room']

        labels = {
            'date_of_adm': 'Date of Admission',
            'date_of_discarge': 'Date of Discharge'
        }

    def __init__(self, *args, **kwargs):
        super(In_patientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

        self.helper.layout = Layout(
            'patient',
            MultiWidgetField(
                'date_of_adm',
                attrs=(
                    {'style': 'width: 30%; display: inline-block;'}
                )
            ),
            MultiWidgetField(
                'date_of_discarge',
                attrs=(
                    {'style': 'width: 30%; display: inline-block;'}
                )
            ),
            'diagnosis',
            'doctor',
            'room',
        )

    def clean(self):
        cleaned_data = super(In_patientForm, self).clean()
        return cleaned_data


class Out_patientForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Out_patient
        fields = ['patient', 'date', 'diagnosis', 'doctor']

    def __init__(self, *args, **kwargs):
        super(Out_patientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

        self.helper.layout = Layout(
            'patient',
            MultiWidgetField(
                'date',
                attrs=(
                    {'style': 'width: 30%; display: inline-block;'}
                )
            ),
            'doctor',
            'diagnosis',
        )

    def clean(self):
        cleaned_data = super(Out_patientForm, self).clean()
        return cleaned_data
