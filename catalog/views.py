# coding=utf-8
from django.shortcuts import render

# Create your views here.

from .models import Product

def product_list(request):
    context = {
        'product_list': Product.objects.all()
    }
    #Sistema de templates procura em cada aplicação especifica
    return render(request, 'product_list.html',context)