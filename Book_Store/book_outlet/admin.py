from django.contrib import admin
from .models import Book, Author,Address, Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author","rating",)
    list_display = ("author","title")
    

class AutherAdmin(admin.ModelAdmin):
  
    list_display = ("first_name","last_name","id","show_city")
    list_filter = ("first_name","last_name")
    
    def show_city(self,obj):
        return obj.address.city    
    
    show_city.short_description ="City"

    


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AutherAdmin)
admin.site.register(Address)
admin.site.register(Country)