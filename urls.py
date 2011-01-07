from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()
from django.conf import settings


urlpatterns = patterns('',

    (r'^$',               include('player.urls')),
	(r'^accounts/',       include('registration.urls')),
	(r'^profile/',        include('profile.urls')),
	(r'^artists/',        include('artists.urls')),
	(r'^contact/',        include('contact.urls')),
		
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)