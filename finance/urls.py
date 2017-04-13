from django.conf.urls import url
from django.contrib import admin
from .views import BillingCreateView

app_name = 'finance'

urlpatterns = [
    url(r'^billing$', BillingCreateView.as_view(), name='billing'),
]
