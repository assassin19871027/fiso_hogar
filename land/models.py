from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Apartment(models.Model):
    unique_key = models.CharField(max_length=31)
    location = models.CharField(max_length=255)
    land_area = models.DecimalField(decimal_places=0,max_digits=3)
    building_area = models.DecimalField(decimal_places=0,max_digits=3)
    living_room = models.DecimalField(decimal_places=0,max_digits=2)
    bathroom = models.DecimalField(decimal_places=0,max_digits=2)
    parking_lot = models.DecimalField(decimal_places=0,max_digits=2)
    # old year of building
    antiquity = models.DecimalField(decimal_places=0,max_digits=2)
    provision = models.DecimalField(decimal_places=0,max_digits=2)
    # including rooms
    ambientes = models.CharField(max_length=255)
    description = models.CharField(max_length=511)
    rent_price = models.DecimalField(decimal_places=0,max_digits=10)
    tag_line = models.CharField(max_length=127)
    image_url = models.CharField(max_length=63)

    class Meta:
        ordering = ['-unique_key']

    def __unicode__(self):
       return self.unique_key

    def image_as_list(self):
        return self.image_url.split(', ')
