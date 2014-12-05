# -*- coding: utf-8 -*-
#============================================================
# Contains functions to handle requests from viewer
# Renders html according to viewer requests
# Last modified: 11/30/2014
#============================================================
from django.shortcuts import render
from django.template import RequestContext
from django.core.context_processors import csrf # csrf - cross site request forgery. 
from equitytrading.forms import *
from equitytrading.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
	'''
	display the main page
	'''
	return render(request, 'index.html')

def hiw(request):
	'''
	display "How It Works" page
	'''
	return render(request, 'info.html', {'type': 'hiw'})
	
def about(request):
	'''
	display "About" page
	'''
	return render(request, 'info.html', {'type': 'about'})

def startups(request):
	'''
	display info page for startups
	'''
	startup_list = Startup.objects.all().order_by('name')
	context_dict = {'list': startup_list, 'type': 'startup'}

	return render(request, 'profiles.html', context_dict)

def businesses(request):
	'''
	display info page for professionals 
	'''
	biz_list = Business.objects.all().order_by('name')
	context_dict = {'list': biz_list, 'type': 'biz'}
	
	# display restricted profiles
	return render(request, 'profiles.html', context_dict)

def registration(request):
	'''
	display registrations page
	'''
	registered = False 								# registration is successful?
	if request.method == 'POST':					# HTTP POST
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()						# save profiles
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit = False)
			profile.user = user
			profile.save()
			registered = True						# register successful
		else:
			print user_form.errors, profile_form.errors
	else:											# not HTTP POST
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request, 'registration.html', 
				  	{'user_form': user_form, 
					'profile_form': profile_form, 
					'registered': registered} 
					)

def user_login(request):
	'''
	display login page
	'''
	if request.method == 'POST':
		username = request.POST['username']	
		password = request.POST['password']
		user = authenticate(username = username, password = password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/myaccount/')				# go to my account 
			else: 											# not active account
				return HttpResponse("Your account is disabled.")
		else:												# invalid username or password
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:													# not HTTP POST
		return render(request, 'login.html', {})

@login_required												# require login
def user_account(request):
	'''
	user account page
	'''	
	user_profile = UserProfile.objects.get(user = request.user)
	category = user_profile.category			

	if category == 'S':						# startup
		if request.method == 'POST':
			form = StartupForm(data = request.POST)
			if form.is_valid():
				form.save()
			else:
				print form.errors
		else:								# not POST
			form = StartupForm()
	else:											# business
		if request.method == 'POST':
			form = BusinessForm(data = request.POST)
			if form.is_valid():
				form.save()
			else:
				print form.errors
		else:								# not POST
			form = BusinessForm()

	return render(request, 'useraccount.html', {
		'form': form
		})

@login_required												# require login
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')
