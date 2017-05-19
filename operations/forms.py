from django import forms
from operations.models import Treatment

# crispy_forms imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, MultiWidgetField, Submit

class TreatmentForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Treatment
        fields = ['patient', 'doctor', 'date', 'symptoms', 'diagnosis', 'doctors_comments']

        labels = {
            'doctors_comments': "Doctor's Comments"
            }

        widgets = {
            'date': forms.SelectDateWidget(years=[str(val) for val in range(1998, 2017)]),
            'symptoms': forms.Textarea(attrs={'rows':4, 'style':'resize:none;'}),
            'doctors_comments': forms.Textarea(attrs={'rows':4, 'style':'resize:none;'}),
            }

    def __init__(self, *args, **kwargs):
        super(TreatmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.fields['symptoms'].widget.attrs['style'] = 'resize:none' //setting textarea resize to none
        # self.helper.form_class = 'form-horizontal'
        # self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Save'))
        self.helper.form_tag = False

        self.helper.layout = Layout(
            'patient',
            'doctor',
            MultiWidgetField(
                'date',
                attrs=(
                    {'style': 'width: 32.8%; display: inline-block;'}
                )
            ),
            'symptoms',
            'diagnosis',
            'doctors_comments',
        )


    def clean(self):
        cleaned_data = super(TreatmentForm, self).clean()
        return cleaned_data
