from django.conf.urls import url
from django.contrib import admin
from .views import IndexView, DiagnoseCreateView, RoomCreateView

app_name = 'malaika'

urlpatterns = [
    url(r'^index', IndexView.as_view(), name='index'),
    url(r'^room$', RoomCreateView.as_view(), name='room'),
    url(r'^diagnose$', DiagnoseCreateView.as_view(), name='diagnose'),
    # url(r'^', IndexView.as_view(), name='index'),
]
