from django.conf.urls import url
from django.contrib import admin
from reception.views import PatientCreateView, In_patientCreateView, Out_patientCreateView, PatientListView, In_patientListView

app_name = 'reception'

urlpatterns = [
    url(r'^patient$', PatientCreateView.as_view(), name='patient'),
    url(r'^patients$', PatientListView.as_view(), name='patients'),
    url(r'^in-patient$', In_patientCreateView.as_view(), name='in_patient'),
    url(r'^out-patient$', Out_patientCreateView.as_view(), name='out_patient'),
]
