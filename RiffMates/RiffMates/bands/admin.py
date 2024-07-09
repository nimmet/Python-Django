from django.contrib import admin
from bands.models import Musician, Room, Venue, Band



# Register your models here.
class MusicianAdmin(admin.ModelAdmin):
    list_display = ("id","last_name","show_weekday")
    search_fields = ("first_name","last_name",)
    
    
    def show_weekday(self,obj):
        return obj.birth.strftime("%A")
    
    show_weekday.short_description ="Birth Weekday"
    

admin.site.register(Musician, MusicianAdmin)
admin.site.register(Venue)
admin.site.register(Room)
admin.site.register(Band)