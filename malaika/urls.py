from django.conf.urls import url
from django.contrib import admin
from .views import IndexView

app_name = 'hospital'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', IndexView.as_view(), name='index'),
]
