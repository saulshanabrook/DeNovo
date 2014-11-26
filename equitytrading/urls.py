#=========================================================
# url mappings
# Last Modified: 11/26/2014
#=========================================================
from django.conf.urls import patterns, url
from equitytrading import views

urlpatterns = patterns('',
        url(r'^home/', views.home, name = 'home'),
		url(r'^startup/', views.startups, name = 'startup'),
		url(r'^business/', views.businesses, name = 'business'),
		url(r'^register/', views.registration, name = 'registration'))