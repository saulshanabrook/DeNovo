# -*- coding: utf-8 -*-
#============================================================
# Contains functions to handle requests from viewer
# Renders html according to viewer requests
# Last modified: 11/26/2014
#============================================================
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf # csrf - cross site request forgery. 
from equitytrading.forms import *
from equitytrading.models import *

# display main page
def home(request):
	#context = RequestContext(request)
	context_dict = {}

	return render(request, 'index.html', context_dict)

# dispaly info page for startups
def startups(request):
	startup_list = Startup.objects.all().order_by('name')
	#context = RequestContext(request)
	context_dict = {'startups': startup_list}

	return render(request, 'info.html', context_dict)

# display info page for professionals 
def businesses(request):
	biz_list = Business.objects.all().order_by('name')
	#context = RequestContext(request)
	context_dict = {'business': biz_list}
	
	# dispaly restricted profiles
	return render(request, 'info.html', context_dict)

# display registrations page
def registration(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()					# save user data
			user.set_password(user.password)		# hash password
			user.save()								# update object
			profile = profile_form.save(commit = False)		# 
			profile.user = user
			profile.phone = profile_form.phone
			profile.save()
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render('registration.html', 
				  	{'user_form': user_form, 
					'profile_form': profile_form, 
					'registered': registered}, 
					context)

