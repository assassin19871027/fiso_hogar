from django.shortcuts import render, render_to_response
from django.template import RequestContext
from .models import Apartment, Guest
from django.db.models import Q

# Create your views here.

def show_index(request):
    message = ''
    rent_price = ''
    bedroom = ''
    bathroom = ''
    num_rent_price = 0
    num_bedroom = 0
    num_bathroom = 0
    if request.method == 'POST':
        postdata = request.POST.copy()
        if postdata['submit'] == 'Filter':
            rent_price = postdata['rent_price']
            bedroom = postdata['bedroom']
            bathroom = postdata['bathroom']
            num_rent_price = int('0' + rent_price)
            num_bedroom = int('0' + bedroom)
            num_bathroom = int('0' + bathroom)

            apartments = Apartment.objects.filter(Q(rent_price__contains=num_rent_price) | Q(living_room__contains=num_bedroom) | Q(bathroom=num_bathroom))
            context = {'apartments': apartments}
            return render(request, 'land/index.html', context)

        if postdata['submit'] == 'GO':
            where = postdata['where']
            price = postdata['price']
            num_price = int('0' + price)
            if num_price == 0:
                apartments = Apartment.objects.filter(Q(location__contains=where))
                context = {'apartments': apartments}
                return render(request, 'land/index.html', context)
            if not where:
                apartments = Apartment.objects.filter(Q(rent_price__contains=num_price))
                context = {'apartments': apartments}
                return render(request, 'land/index.html', context)

            apartments = Apartment.objects.filter(Q(location__contains=where) | Q(rent_price__contains=num_price))
            context = {'apartments': apartments}
            return render(request, 'land/index.html', context)


        if postdata['submit'] == 'Subscribe	to	our	mailing	list':

            place_temp = False
            area_temp = False
            finding_place_temp = False
            process_temp = False
            place = request.POST.getlist('place')
            area = request.POST.getlist('area')
            finding_place = request.POST.getlist('finding_place')
            process = request.POST.getlist('process')
            if place:
                place_temp = True
            if area:
                area_temp = True
            if finding_place:
                finding_place_temp = True
            if process:
                process_temp = True

            full_name = postdata['full_name']
            email = postdata['email']
            daytime_phone = postdata['daytime_phone']
            bedroom = postdata['bedroom']
            price = postdata['price']
            location_area = postdata['location_area']
            guest = Guest.objects.filter(Q(full_name=full_name) | Q(email=email) | Q(daytime_phone=daytime_phone) | Q(bedroom=bedroom) | Q(price=price) | Q(location_area=location_area))
            if guest:
                message = 'Guest information is already registered correctly.'
            else:
                guest = Guest(place=place_temp, area=area_temp, finding_place=finding_place_temp, process=process_temp, full_name=full_name, email=email, daytime_phone=daytime_phone, bedroom=bedroom, price=price, location_area=location_area)
                guest.save()
                message = 'Guest information is registered correctly.'

    apartments = Apartment.objects.all();
    context = {'apartments': apartments, 'message': message}
    return render(request, 'land/index.html', context)
