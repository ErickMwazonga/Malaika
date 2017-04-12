from django.forms import forms
from malaika.models import Diagnose, Room


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

    def clean(self):
        cleaned_data = super(RoomForm, self).clean()
        return cleaned_data


class DiagnoseForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Diagnose
        fields = ['name', 'code', 'description']

    def __init__(self, *args, **kwargs):
        super(DiagnoseForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(DiagnoseForm, self).clean()
        return cleaned_data
