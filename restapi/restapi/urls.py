'''
Created on Apr 28, 2014

@author: Piyush Mittal
'''
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', 'restapi.views.api_root', name='api-root'),
    url(r'^server/$', views.ServerList.as_view(), name='server-list'),
    url(r'^server/(?P<pk>.*)/$', views.ServerDetail.as_view(), name='server-detail'),
    )
