from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'findburo.views.index'),
    url(r'^category/(?P<key>\w+)/$', 'reccomendation.views.category_reccomendations'),
    # url(r'^findburo/', include('findburo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<category>\w+)/$', 'findburo.views.index'),
)
