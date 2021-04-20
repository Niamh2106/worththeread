from django.shortcuts import render
from django.http import HttpResponse
from . models import Page

def index(request, pagename = ''):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
	'title':pg.title,
	'content':pg.bodytext,
    }
    return render(request, 'base.html', context)

# Create your views here.