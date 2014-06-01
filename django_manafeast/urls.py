from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_manafeast.views.home', name='home'),
    url(r'^account.html$', 'accounts.views.new_account'),
    url(r'^donate.html$', 'donations.views.donate'),
    url(r'^ajax/', include('ajax.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ) # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #      static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)]
