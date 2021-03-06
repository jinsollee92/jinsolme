from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^blog/$', views.blog),
	url(r'^blog/page=(?P<page>[0-9]+)/$', views.blog),
	url(r'^blog/category/(?P<category>[a-zA-Z0-9_-]+)/$', views.blog),
	url(r'^blog/category/(?P<category>[a-zA-Z0-9_-]+)/page=(?P<page>[0-9]+)/$', views.blog),
	url(r'^blog/post/(?P<post>[a-zA-Z0-9_-]+)/$', views.blog),
	url(r'^about/$', views.about),
	url(r'^contact/$', views.contact),
]