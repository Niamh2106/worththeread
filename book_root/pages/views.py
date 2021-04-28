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
    template ="index.html" if pagename == "/" else pagename[1:] + ".html"
    return render(request, template, context)

# def home(request):
#     return render(request, "home.html")

# class SearchResultsView(ListView):
#     model = Page
#     template_name = 'search_results.html'

# Create your views here.