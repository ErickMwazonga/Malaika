from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import IndexView, RoomListView, DiagnoseListView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

app_name = 'malaika'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^room$', views.room_create, name='room_create'),
    url(r'^room/(?P<pk>\d+)/update/$', views.room_update, name='room_update'),
    url(r'^room/(?P<pk>\d+)/delete/$', views.room_delete, name='room_delete'),
    url(r'^rooms$', RoomListView.as_view(), name='rooms'),
    url(r'^diagnose$', views.diagnose_create, name='diagnose_create'),
    url(r'^diagnose/(?P<pk>\d+)/update/$', views.diagnose_update, name='diagnose_update'),
    url(r'^diagnose/(?P<pk>\d+)/delete/$', views.diagnose_delete, name='diagnose_delete'),
    url(r'^diagnoses$', DiagnoseListView.as_view(), name='diagnoses'),
    url(r'^login$', auth_views.login, {
            'template_name': 'malaika/login.html',
            'authentication_form': AuthenticationForm
        },
        name='login'
    ),
    url(r'^logout/$', auth_views.logout_then_login, {'login_url':'malaika:login'}, name='logout'),
]
