#-*- coding:utf-8 -*-
from django.contrib import admin
from xadmin.views import CommAdminView
import xadmin

class GlobalSetting(object):
	site_title = '博客群组'
	site_footer = '@skyleft'

xadmin.site.register(CommAdminView, GlobalSetting)
# Register your models here.
