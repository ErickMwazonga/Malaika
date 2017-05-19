from django import forms
from malaika.models import Diagnose, Room

# crispy_forms imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import  Submit

class RoomForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Room
        fields = ['room_number', 'room_type']

        labels = {
            'room_number': 'Room Number',
            'room_type': 'Room Type'
        }

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_class = 'form-horizontal'
        # self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Save'))
        self.helper.form_tag = False

    def clean(self):
        cleaned_data = super(RoomForm, self).clean()
        return cleaned_data


class DiagnoseForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Diagnose
        fields = ['name', 'code', 'description']

        widgets = {
            "description": forms.Textarea(
                attrs={'rows':4, 'style':'resize:none;'}
                )
            }

    def __init__(self, *args, **kwargs):
        super(DiagnoseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_class = 'form-horizontal'
        # self.helper.form_method = 'post'
        self.helper.form_tag = False
        # self.helper.add_input(Submit('submit', 'Save'))

    def clean(self):
        cleaned_data = super(DiagnoseForm, self).clean()
        return cleaned_data
