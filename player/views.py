from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf.urls.defaults import *
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template import Context, loader
from django.contrib.auth import authenticate


def index(request):
	
	return render_to_response('player/index.html', {}, context_instance=RequestContext(request))

