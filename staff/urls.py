from django.conf.urls import url
from django.contrib import admin
from .views import DoctorCreateView

app_name = 'staff'

urlpatterns = [
    url(r'^doctor$', DoctorCreateView.as_view(), name='doctor'),
]
