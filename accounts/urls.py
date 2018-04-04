from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

app_name = 'accounts'

urlpatterns = [
    url(r'^login$', auth_views.login, {
            'template_name': 'accounts/login.html',
            'authentication_form': AuthenticationForm
        },
        name='login'
    ),
    url(r'^logout/$', auth_views.logout_then_login, {'login_url':'accounts:login'}, name='logout'),
]
