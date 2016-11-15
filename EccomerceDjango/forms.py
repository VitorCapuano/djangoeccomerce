# coding=utf-8

from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(label = 'Nome',required=True)
    email = forms.EmailField(label = 'E-mail',required=True)
    mensagem = forms.CharField(label='Mensagem',widget=forms.Textarea(), required=False)


    #def __init__(self, *args, **kwargs):
        #super(ContactForm,self).__init__(*args,**kwargs)
        #self.fields['name'].widget.attrs['class'] = 'form-control'
        #self.fields['email'].widget.attrs['class'] = 'form-control'
        #self.fields['mensagem'].widget.attrs['class'] = 'form-control'

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['mensagem']
        message = 'Nome: {0}\nE-mail:{1}\n{2}'.format(name, email, message)
        send_mail('Contato do Django E-ccomerce',
                  message, settings.DEFAULT_FROM_EMAIL,
                  [settings.EMAIL_BACKEND])
        sucesso = True
