from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

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

def database(request):
    return render(request, 'publications.html')

def contact(request):
    return render(request, 'contact.html')
