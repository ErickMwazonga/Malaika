from django import forms
from reception.models import Patient, In_patient, Out_patient

# crispy_forms imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, MultiWidgetField, Submit, Div, Fieldset
from crispy_forms.bootstrap import Field

class PatientForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'dob', 'age', 'country', 'city', 'address', 'contact_no', 'next_of_kin']

        labels = {
            'dob': 'Date of Birth',
            'contact_no': 'Contact Number'
        }
        widgets = {
            'dob': forms.SelectDateWidget(years=[str(val) for val in range(1998, 2005)]),
            }


    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

        self.helper.layout = Layout(
            'first_name','last_name','gender',
                    MultiWidgetField(
                        'dob',
                        attrs=(
                            {'style': 'width: 32.8%; display: inline-block;'}
                        )
                    ), 'age',
            Fieldset('Contact Information',
                Field('country', 'city','address', 'contact_no', 'next_of_kin')
            )
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
        widgets = {
            'date_of_adm': forms.SelectDateWidget(years=[str(val) for val in range(1998, 2017)]),
            'date_of_discarge': forms.SelectDateWidget(years=[str(val) for val in range(1998, 2017)]),
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
                    {'style': 'width: 32.8%; display: inline-block;'}
                )
            ),
            MultiWidgetField(
                'date_of_discarge',
                attrs=(
                    {'style': 'width: 32.8%; display: inline-block;'}
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

        widgets = {
            'date': forms.SelectDateWidget(years=[str(val) for val in range(1998, 2017)]),
            }

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
                    {'style': 'width: 32.8%; display: inline-block;'}
                )
            ),
            'doctor',
            'diagnosis',
        )

    def clean(self):
        cleaned_data = super(Out_patientForm, self).clean()
        return cleaned_data
