from django.conf.urls import url
from django.contrib import admin
from malaika.views import IndexView

app_name = 'malaika'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', IndexView.as_view(), name='index'),
]
