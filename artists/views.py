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


def create_artist(request):
	return HttpResponse("Hi :D")

def edit_artist(request):
	return HttpResponse("Hi edit me :D")

def artist_detail(request, artistname):
	return HttpResponse("Hi details for :D"+artistname)

def artist_list(request):
	return HttpResponse("Hi list them:D")
