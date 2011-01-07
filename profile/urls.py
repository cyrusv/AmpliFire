from django.conf.urls.defaults import *
from profile import views
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
                       url(r'^create/$',
                           views.create_profile,
                           name='profiles_create_profile'),
                       url(r'^edit/$',
                           views.edit_profile,
                           name='profiles_edit_profile'),
                       url(r'^(?P<username>\w+)/$',
                           views.profile_detail,
                           name='profiles_profile_detail'),
                       url(r'^$',
                           views.profile_list,
                           name='profile_list'),
                       )
