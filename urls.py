from django.conf.urls.defaults import *
    from django.contrib import admin

    admin.autodiscover()

urlpatterns = patterns('',
(r'^rest/', include('eatrack.app.rest.urls')),
    (r'^admin/', include(admin.site.urls)),
    # (r'^media/(.*)$', 'django.views.static.serve', {'document_root': 'media', 'show_indexes': True}),
)
