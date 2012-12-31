from django.conf.urls import patterns, include, url
from app1.views import hello_view

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'megatemplate.views.home', name='home'),
    # url(r'^megatemplate/', include('megatemplate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view=hello_view, name='hello_page'),
)