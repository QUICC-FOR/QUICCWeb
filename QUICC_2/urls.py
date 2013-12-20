from django.conf.urls import patterns, include, url
from QUICC_2.views import *

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
    url(r'^home/$', 'QUICC_2.views.home', name='home'),
    url(r'^res/$', 'QUICC_2.views.research', name='research'),
    url(r'^team/$', 'QUICC_2.views.team', name='team'),
    url(r'^db/$', 'QUICC_2.views.database', name='database'),
    url(r'^cont/$', 'QUICC_2.views.contact', name='contact'),
)
