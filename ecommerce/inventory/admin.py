from django.contrib import admin
from .models import *


# Register your models here.




class CategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields = {
    #     "slug":("name",)
    # }
    
    list_display = ("id","name","slug")
    search_fields = ["name","slug"]
    list_display_links = ("id",)
    list_editable = ("name",)
    
    

class ProductAdmin(admin.ModelAdmin):  
    list_filter = ("stock_status",)  
    # inlines = ["ProductLineInline"]
    

class ProductLineInline(admin.StackedInline):
    model = ProductLine
    extra = 1
    

class ChildCategoryInline(admin.TabularInline):
    model = Category
    fk_name = "parent"
    extra = 1
    
class ParentCategoryAdmin(admin.ModelAdmin):
    inline = [ChildCategoryInline]
    list_display = ("name","parent_name",)
    
    def parent_name(self, obj):
        return obj.parent.name if object else None
    
 
class ChildTypeInline(admin.TabularInline):
    model = "ProductType"
    fk_name = "parent"
    extra = 1 
    

class ParentTypeAdmin(admin.ModelAdmin):
    inline = [ChildTypeInline]
     
 
class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    
class AttributeAdmin(admin.ModelAdmin):
    inline = [AttributeValueInline]
    
class SeasonalEventsAdmin(admin.ModelAdmin):
    list_display = ("name","start_date","end_date",)
    

class ProductLineInline(admin.StackedInline):
    model = ProductLine
    extra = 1
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]
    list_display = ("name","category","stock_status","is_active",)
    list_filter = (
        "category","stock_status","is_active",
    )
    search_fields = ("name",)
    
    
admin.site.register(Product,ProductLineInline) 
admin.site.register(Category, ParentCategoryAdmin)
admin.site.register(ProductLine)
admin.site.register(ProductImage)
admin.site.register(ProductType, ParentTypeAdmin)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(SeasonalEvents, SeasonalEventsAdmin)





