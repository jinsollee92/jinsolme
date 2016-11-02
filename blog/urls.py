from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^blog/$', views.blog),
	url(r'^blog/?page=(?P<num>[0-9]+)/$', views.blog),
]