from django.conf.urls import url
from django.contrib import admin
from .views import DoctorListView
from . import views

app_name = 'staff'

urlpatterns = [
    url(r'^doctor$', views.doctor_create, name='doctor_create'),
    url(r'^doctor/(?P<pk>\d+)/update/$', views.doctor_update, name='doctor_update'),
    url(r'^doctor/(?P<pk>\d+)/delete/$', views.doctor_delete, name='doctor_delete'),
    url(r'^doctors$', DoctorListView.as_view(), name='doctors'),
]
