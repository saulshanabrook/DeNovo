#===========================================================
# sign up forms for online profiles and accounts
# Last Modified: 11/26/2014
#===========================================================
from django import forms
from equitytrading.models import *
from django.contrib.auth.models import User

class StartupForm(forms.ModelForm):
	'''
	form for startup online profile
	'''
	# required fields
	name = forms.CharField(max_length = 100, help_text = "Name of Your Venture?")
	logo = forms.ImageField(help_text = "Upload Your Logo here")
	location = forms.CharField(max_length = 100, help_text = "Location of your office?")
	industry = forms.CharField(max_length = 200, help_text = "Industry Sector?")
	description = forms.CharField(max_length = 5000, help_text = "Description of your venture?")
	service_needed = forms.CharField(max_length = 200, help_text = "Service Needed")
	service_detail = forms.CharField(max_length = 2000, help_text = "Details of Service Needed")
	contact_email = forms.EmailField(max_length = 80, help_text = "Contact Email")
	contact_phone_number = forms.CharField(max_length = 15, help_text = "Contact Phone Number")

	class Meta:
		# associate form with the Startup Model
		model = Startup
		# fields in included in the form:
		fields = ('name', 'logo', 'location', 'industry', 'description', 'service_needed', 'service_detail', 'contact_person', 'contact_email', 'contact_phone_number')
		
class BusinessForm(forms.ModelForm):
	'''
	forms for online profiles for companies
	'''
	# required fields
	name = forms.CharField(max_length = 128, help_text = "Name of Company?")
	logo = forms.ImageField(help_text = "Upload Your Logo here")
	location = forms.CharField(max_length = 128, help_text = "Where's your company located?")
	industry = forms.CharField(max_length = 200, help_text = "Industry Sector?")
	type_of_service = forms.CharField(max_length = 200, help_text = "Service Provided?")
	description = forms.CharField(max_length = 5000, help_text = "Description of your company")
	
	class Meta:
		# associate form with the Professional Model
		model = Business
		fields = ('name', 'logo', 'location', 'industry', 'description', 'type_of_service')

class UserForm(forms.ModelForm):
	'''
	UserFrom uses built-in User object
	'''
	password = forms.CharField(widget = forms.PasswordInput())
	
	class Meta:
		# associate form with the User Model
		model = User
		fields = ('username', 'password', 'email')
		
class UserProfileForm(forms.ModelForm):
	'''
	user account form
	'''
	CATEGORY_CHOICES = (
		('S', 'Startup'),
		('B', 'Business'),
	)
	category = 	forms.ChoiceField(widget=forms.RadioSelect, choices=CATEGORY_CHOICES) 			#  startup or professional?
	
	class Meta:
		# associate form with the UserProfile Model
		model = UserProfile
		fields = ('category', )