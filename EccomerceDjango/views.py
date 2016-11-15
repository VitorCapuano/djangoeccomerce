from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import View,TemplateView
# Create your views here.
from EccomerceDjango.forms import ContactForm
from catalog.models import Category

#Criacao de Views por classe, Class Based Views
"""class IndexView(object):

    def __call__(self, request):
        return render(request, 'index.html')"""

"""class IndexView(View):

    #metodo get html
    def get(self, request):
        return render(request, 'index.html')"""

class IndexView(TemplateView):

    #metodo get html
    template_name = 'index.html'


index = IndexView.as_view()


def contact(request):
    sucesso = False
    form = ContactForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.send_mail()
            sucesso = True
            return render(request, 'contact.html', {
        'form':ContactForm(None),
        'sucesso':sucesso
    })
    return render(request, 'contact.html', {
        'form':form,
        'sucesso':sucesso
    })

