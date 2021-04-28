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
    template ="index.html"
    return render(request, template, context)

# class SearchResultsView(ListView):
#     model = Page
#     template_name = 'search_results.html'

# Create your views here.