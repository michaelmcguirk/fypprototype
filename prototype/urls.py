from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'prototype.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^temps/', include('temps.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
