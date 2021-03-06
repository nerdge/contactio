"""contact_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

import core
from core.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core.views.contact_list, name='contacts'),
    url(r'^new/$', core.views.contact_new, name='contact_new'),
    url(r'^/(?P<pk>[0-9]+)/edit/$', core.views.contact_edit, name='contact_edit'),
    url(r'^/(?P<pk>[0-9]+)/delete/$', core.views.contact_delete, name='contact_delete'),
    url(r'^login/$', 'core.views.login_user', name="login_user"),
    url(r'^logout/$', 'core.views.logout_user', name='logout_user'),
    url(r'^signup/$', 'core.views.register_user', name='register_user'),
]
