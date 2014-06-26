from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import render_to_response
from publications.models import Publication
import datetime

def get_publi(request):

        publi = Publication.objects.order_by('-year')
        dicPubli = {
            "publi_details" : publi
        }

        return render_to_response('publications.html',dicPubli, context_instance=RequestContext(request))

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    return render(request, 'home.html')

def research(request):
    return render(request, 'research.html')

def team(request):
    return render(request, 'team.html')

def database(request):
    return render(request, 'database.html')

def contact(request):
    return render(request, 'contact.html')
