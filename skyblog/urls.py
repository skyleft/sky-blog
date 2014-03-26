from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.static import serve
from account import urls as accountUrls
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skyblog.views.home', name='home'),
    # url(r'^skyblog/', include('skyblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/',include(accountUrls)),
    url(r'^$','blog.views.index'),
    url(r'^post/(?P<post_id>\d+)/$','blog.views.post'),
    url(r'^category/(?P<category_id_tmp>\d+)/$','blog.views.category'),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    url(r'^comment/$','blog.views.comment')
)

