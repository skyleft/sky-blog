__author__ = 'Administrator'
from models import Post,Category,Tag,Blog
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    list_display = ['name']

class PostAdmin(admin.ModelAdmin):
    list_display = ['name','category','content','pub_date']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','alias']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name','alias']

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Blog,BlogAdmin)