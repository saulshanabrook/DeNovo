#=========================================================
# url mappings
# Last Modified: 11/26/2014
#=========================================================
from django.conf.urls import patterns, url
from equitytrading import views

urlpatterns = patterns('',
        url(r'^$', views.home, name = 'home'),
		url(r'^how-it-works/', views.hiw, name = 'how-it-works'),
		url(r'^about/', views.about, name = 'about'),
		url(r'^startup/', views.startups, name = 'startup'),
		url(r'^business/', views.businesses, name = 'business'),
		url(r'^register/', views.registration, name = 'registration'),
		url(r'^login/', views.user_login, name = 'login'))