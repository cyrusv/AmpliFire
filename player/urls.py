from django.conf.urls.defaults import *
from player.views import index
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
                       url(r'^$',
                           index,
                           name='index'),
                       )
