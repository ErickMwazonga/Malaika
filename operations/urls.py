from django.conf.urls import url
from django.contrib import admin
from .views import TreatmentListView
from . import views

app_name = 'operations'

urlpatterns = [
    url(r'^treatment$', views.treatment_create, name='treatment_create'),
    url(r'^treatment/(?P<pk>\d+)/update/$', views.treatment_update, name='treatment_update'),
    url(r'^treatment/(?P<pk>\d+)/delete/$', views.treatment_delete, name='treatment_delete'),
    url(r'^treatments$', TreatmentListView.as_view(), name='treatments'),
]
