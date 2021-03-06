from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.static import serve
from account import urls as accountUrls
from blog import blogurls
import settings
#admin.autodiscover()
import xadmin
xadmin.autodiscover()

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns('',
    url(r'xadmin/', include(xadmin.site.urls)),
)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'skyblog.views.home', name='home'),
    # url(r'^skyblog/', include('skyblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^account/',include(accountUrls)),
    url(r'^test/',include(blogurls)),
    url(r'^$','blog.views.index'),
    url(r'^post/(?P<post_id>\d+)/$','blog.views.post'),
    url(r'^post/vote/(?P<post_id>\d+)/$','blog.views.vote'),
    url(r'^category/(?P<category_id_tmp>\d+)/$','blog.views.category'),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    url(r'^comment/$','blog.views.comment')
)

