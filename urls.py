from django.conf.urls import patterns, url

from brewlog import views

urlpatterns = patterns('',
                       url(r'^brewdays$', views.index, name='index'),
                       url(r'^brewdays/(?P<brewday_id>\d+)/$', views.detail, name='detail'),
)