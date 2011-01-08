from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.context_processors import auth as auth_context_processor
from django.views.generic.list_detail import object_list
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from artists.models import Artist, Album, Song


def create_artist(request):
	return render_to_response('artists/create_artist.html', context_instance=RequestContext(request))

def edit_artist(request, artistname):
	artist = get_object_or_404(Artist, artistname=artistname)
	fields = artist.get_fields()
	return render_to_response('artists/edit_artist.html', {'fields': fields, 'artist':artist }, context_instance=RequestContext(request))

def artist_detail(request, artistname):
	artist = get_object_or_404(Artist, artistname=artistname)
	return render_to_response('artists/artist_detail.html', {'artist':artist}, context_instance=RequestContext(request))

def artist_list(request):
	return render_to_response('artists/artist_list.html', context_instance=RequestContext(request))
