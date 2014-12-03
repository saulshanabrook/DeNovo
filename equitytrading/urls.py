#=========================================================
# url mappings
# Last Modified: 11/30/2014
#=========================================================
from django.conf.urls import patterns, url
from equitytrading import views
from django.conf import settings

urlpatterns = patterns('',
        url(r'^$', views.home),
        url(r'^home/', views.home, name = 'home'),
		url(r'^how-it-works/', views.hiw, name = 'how-it-works'),
		url(r'^about/', views.about, name = 'about'),
		url(r'^startup/', views.startups, name = 'startup'),
		url(r'^business/', views.businesses, name = 'business'),
		url(r'^register/', views.registration, name = 'registration'),
		url(r'^login/', views.user_login, name = 'login'),
		url(r'^myaccount/', views.user_account, name = 'myaccount'),
		url(r'^logout/', views.user_logout, name = 'logout'),
		)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )