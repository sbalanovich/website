from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'', include('visualization.urls')),
    url(r'^visualization/', include('visualization.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
