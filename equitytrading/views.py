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

USERNAME = ''

def home(request):
	'''
	display the main page
	'''
	return render(request, 'index.html')

def hiw(request):
	'''
	display "How It Works" page
	'''
	return render(request, 'info.html')
	
def about(request):
	'''
	display "About" page
	'''
	return render(request, 'info.html')

def startups(request):
	'''
	dispaly info page for startups
	'''
	startup_list = Startup.objects.all().order_by('name')
	context_dict = {'startups': startup_list}

	return render(request, 'profiles.html', context_dict)

def businesses(request):
	'''
	display info page for professionals 
	'''
	biz_list = Business.objects.all().order_by('name')
	context_dict = {'business': biz_list}
	
	# dispaly restricted profiles
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
			user_form.save()						# save profiles
			profile_form.save()
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
				USERNAME = username
				login(request, user)
				return HttpResponseRedirect('/myaccount/')				#! need to fill in with page 
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
	#username = request.user.username				# get user info
	user = UserProfile.objects.get(username = USERNAME)			# get the usr object????
	category = user.categrory			

	if category == 'startup':						# startup
		if request.method == 'POST':
			form = StartupForm(data = request.POST)
		else:
			form = StartupForm()
	else:											# business
		if request.method == 'POST':
			form = BusinessForm(data = request.POST)
		else:
			form = BusinessForm()

	return render(request, 'useraccount.html', {
		'form': form
		})

@login_required												# require login
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/home/')
