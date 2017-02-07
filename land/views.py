from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import Apartment
from django.db.models import Q

# Create your views here.

def show_index(request):
    rent_price = ''
    bedroom = ''
    bathroom = ''
    num_rent_price = 0
    num_bedroom = 0
    num_bathroom = 0
    if request.method == 'POST':
        postdata = request.POST.copy()
        rent_price = postdata['rent_price']
        bedroom = postdata['bedroom']
        bathroom = postdata['bathroom']
        num_rent_price = int('0' + rent_price)
        num_bedroom = int('0' + bedroom)
        num_bathroom = int('0' + bathroom)

        apartments = Apartment.objects.filter(Q(rent_price=num_rent_price) | Q(living_room=num_bedroom) | Q(bathroom=num_bathroom))
        context = {'apartments': apartments}
        return render(request, 'land/index.html', context)

    apartments = Apartment.objects.all();
    context = {'apartments': apartments}
    return render(request, 'land/index.html', context)
