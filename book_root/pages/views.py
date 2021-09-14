from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from django.urls import reverse

from . models import Page
from .contact import ContactForm


def index(request, pagename = ''):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
	'title':pg.title,
	'content':pg.bodytext,
    }
    template ="index.html" if pagename == "/" else pagename[1:] + ".html"
    return render(request, template, context)

def contact(request):
	submitted = False
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			con = get_connection('django.core.mail.backends.console.EmailBackend')
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@dcu.ie'),
				['niamh.idehen2@mail.dcu.ie'], # change this
				connection=con
			)
			return HttpResponseRedirect(reverse('contact') + '?submitted=True')
	else:
		form = ContactForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {
		'form': form,
		'page_list': Page.objects.all(),
		'submitted': submitted
	}
	return render(request, 'contact.html', context)

# class SearchResultsView(ListView):
#     model = Page
#     template_name = 'search_results.html'

# Create your views here.