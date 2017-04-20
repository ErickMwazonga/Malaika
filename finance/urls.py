from django.conf.urls import url
from django.contrib import admin
from .views import BillingListView
from . import views

app_name = 'finance'

urlpatterns = [
    url(r'^billing$', views.billing_create, name='billing_create'),
    url(r'^billing/(?P<pk>\d+)/update/$', views.billing_update, name='billing_update'),
    url(r'^billing/(?P<pk>\d+)/delete/$', views.billing_delete, name='billing_delete'),
    url(r'^billings$', BillingListView.as_view(), name='billings'),
]
