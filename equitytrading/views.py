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
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

# display main page
def home(request):
	#context = RequestContext(request)
	context_dict = {}

	return render(request, 'index.html', context_dict)
	
# display "How It Works" page
def hiw(request):
	context_dict = {}
	return render(request, 'info.html', context_dict)
	
# display "About" page
def about(request):
	context_dict = {}
	return render(request, 'info.html', context_dict)

# dispaly info page for startups
def startups(request):
	startup_list = Startup.objects.all().order_by('name')
	#context = RequestContext(request)
	context_dict = {'startups': startup_list}

	return render(request, 'profiles.html', context_dict)

# display info page for professionals 
def businesses(request):
	biz_list = Business.objects.all().order_by('name')
	#context = RequestContext(request)
	context_dict = {'business': biz_list}
	
	# dispaly restricted profiles
	return render(request, 'profiles.html', context_dict)

# display registrations page
def registration(request):
	#context = RequestContext(request)
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
			profile.save()
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request, 'registration.html', 
				  	{'user_form': user_form, 
					'profile_form': profile_form, 
					'registered': registered} 
					)

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})