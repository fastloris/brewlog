from django.conf.urls import patterns, url

from brewlog import views

urlpatterns = patterns('',
                       url(r'^brewdays$', views.brewdayindex, name='brewdayindex'),
                       url(r'^brewdays/(?P<brewday_id>\d+)/$', views.brewdaydetail, name='brewdaydetail'),

                       url(r'^recipes$', views.recipeindex, name='recipeindex'),
                       url(r'^recipes/(?P<recipe_id>\d+)/$', views.recipedetail, name='recipedetail'),
)