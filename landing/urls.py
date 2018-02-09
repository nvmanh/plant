from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
  url(r'^landing/$', views.landing, name='landing'),
  url(r'^landing/dashboard/$', views.dashboard, name='dashboard'),
  url(r'^landing/time/plus/(\d{1,2})/$', views.hours_ahead, name='hours_ahead'),
]


urlpatterns += staticfiles_urlpatterns()