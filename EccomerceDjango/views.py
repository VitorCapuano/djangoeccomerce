from django.shortcuts import render

# Create your views here.
from catalog.models import Category
def index(request):

    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')



def product(request):
    return render(request, 'product.html')