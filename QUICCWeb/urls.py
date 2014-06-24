from django.conf.urls import patterns, include, url
from QUICCWeb.views import *

from django.contrib import admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'QUICCFOR.views.home', name='home'),
    # url(r'^QUICCFOR/', include('QUICCFOR.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', welcome),
    url(r'^home/$', 'QUICCWeb.views.home', name='home'),
    url(r'^res/$', 'QUICCWeb.views.research', name='research'),
    url(r'^team/$', 'QUICCWeb.views.team', name='team'),
    url(r'^db/$', 'QUICCWeb.views.database', name='database'),
    url(r'^pub/$', 'QUICCWeb.views.publications', name='publications'),
    url(r'^cont/$', 'QUICCWeb.views.contact', name='contact'),

)
