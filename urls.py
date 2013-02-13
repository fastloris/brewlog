from django.conf.urls import patterns, url

from brewlog import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<brewday_id>\d+)/$', views.detail, name='detail'),
)