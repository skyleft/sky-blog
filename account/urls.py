from django.conf.urls import patterns, include, url
urlpatterns = patterns('account.views',
    url('^register$','reg'),
    url('^complete_profile','complete_profile'),

) 
