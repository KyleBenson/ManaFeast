from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#TODO: remove and do properly in production!
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'django_manafeast.views.login_handler', name='home'),
    url(r'^account.html$', 'accounts.views.new_account'),
    url(r'^donate.html$', 'donations.views.donate'),
    url(r'^search$', 'donations.views.search'),
    url(r'^ajax/', include('ajax.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
