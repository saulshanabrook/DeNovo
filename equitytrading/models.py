#============================================================
# Models for user/online profile objects
# Fields are to be stored in SQLite3 database
# Includes startups, professionals, and a general use profile
# Last Modified: 11/26/2014
#============================================================
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator

# account profile
class UserProfile(models.Model):
	CATEGORY_CHOICES = (
		('S', 'Startup'),
		('B', 'Business'),
	)
	user = 					models.OneToOneField(User)
	date_created = 			models.DateTimeField(default = timezone.now())
	category = 				models.CharField(max_length = 1, choices=CATEGORY_CHOICES) 			#  startup or professional?
														
	# print name field
	def __unicode__ (self):
		return self.user.username

# online profiles
class Startup(models.Model):
	# about startup
	name = 					models.CharField(max_length = 100, unique = True)
	logo = 					models.ImageField()
	date_created = 			models.DateTimeField(default = timezone.now())
	location = 				models.CharField(max_length = 100) 			# dropdown + other for searching
	industry = 				models.CharField(max_length = 200) 			# dropdown box + other
	description = 			models.TextField(max_length = 5000)
	# service needed + contact
	service_needed = 		models.CharField(max_length = 200)     # dropdown
	service_detail = 		models.TextField(max_length = 3000)	# detailed description of service needed
	contact_person = 		models.CharField(max_length = 50)
	contact_email = 		models.EmailField(max_length = 80)
	phone_regex = RegexValidator(regex = r'^\+?1?\d{9,15}$', message = "Phone number must be entered in the format: '+123456789'")
	contact_phone_number = 	models.CharField(max_length = 15) 
	user_profile = 			models.ForeignKey(UserProfile)

	# print name field
	def __unicode__ (self):
		return self.name
		
class Business(models.Model):
	# about the company
	name = 					models.CharField(max_length = 100, unique = True)
	logo = 					models.ImageField()
	date_created = 			models.DateTimeField(default = timezone.now())
	location = 				models.CharField(max_length = 100) 				# dropdown + other for searching
	industry = 				models.CharField(max_length = 200) 				# dropdown box + other
	type_of_service = 		models.CharField(max_length = 100) 		# dropdown
	description = 			models.TextField(max_length = 5000)
	user_profile = 			models.ForeignKey(UserProfile)
	
	# print name field
	def __unicode__ (self):
		return self.name

