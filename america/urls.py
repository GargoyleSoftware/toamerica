from django.conf.urls import patterns, include, url

# enable the admin:
from django.contrib import admin
admin.autodiscover()

from catalog.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'america.catalog.views.home', name='home'),
    url(r'^regionalcenter/$', RegionalCenterListView.as_view(), name='regional-center-list'),
    url(r'^regionalcenter/(?P<pk>\d+)/$', RegionalCenterDetailView.as_view(), name='regional-center-detail'),
    #url(r'^america/', include('america.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
