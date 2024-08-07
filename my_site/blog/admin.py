from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title","author","date")
    list_filter = ("title","tags","author","date")
    prepopulated_fields = {"slug":("title",)}
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name","post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)