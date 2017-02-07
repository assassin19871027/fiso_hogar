from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import Apartment

# Create your views here.

def show_index(request):
    error = ''
    if request.method == 'POST':
        error = 'ok'
    apartments = Apartment.objects.all();
    context = {'apartments': apartments}
    return render(request, 'land/index.html', context)
