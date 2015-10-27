from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core_app.views.home', name='home'),
    url(r'^' + settings.APP_URL_DOMAIN[1:], include('djangologinapp.urls')),
    url(r'^analytics/$', 'core_app.views.analytics', name='analytics'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
