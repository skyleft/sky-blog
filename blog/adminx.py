#-*- coding:utf-8 -*-
__author__ = 'Administrator'
from models import Post,Category,Tag,Blog
import xadmin

class BlogAdmin(object):
	list_filter = ('create_date',)
	list_display = ('name','user')

class PostAdmin(object):
    list_display = ('name','category','pub_date','blog')
    date_hierarchy = 'pub_date'

class CategoryAdmin(object):
    list_display = ('name','alias')

class TagAdmin(object):
    list_display = ('name','alias')

xadmin.site.register(Post,PostAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Blog,BlogAdmin)