from django.contrib import admin
from . models import Apartment

# Register your models here.
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('unique_key', 'location', 'land_area', 'living_room', 'rent_price', 'tag_line')

admin.site.register(Apartment, ApartmentAdmin)
