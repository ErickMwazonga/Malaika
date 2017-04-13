from django.conf.urls import url
from django.contrib import admin
from .views import TreatmentCreateView

app_name = 'operations'

urlpatterns = [
    url(r'^treatment$', TreatmentCreateView.as_view(), name='treatment'),
]
