from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

admin.site.site_header = "Event Management Administration"
admin.site.site_title = "Event Management Administration"

urlpatterns = patterns('',    
    url(r'^registeration/', include('registeration.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', include('registeration.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}),)
