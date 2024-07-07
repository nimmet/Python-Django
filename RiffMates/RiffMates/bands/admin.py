from django.contrib import admin
from bands.models import Musician, Room, Venue



# Register your models here.

admin.site.register(Musician)
admin.site.register(Venue)
admin.site.register(Room)