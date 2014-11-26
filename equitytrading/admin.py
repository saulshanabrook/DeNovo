#=================================================
# settings for DeNovo admin page
# Last Modified: 11/26/2014
#=================================================
from django.contrib import admin
from equitytrading.models import *

admin.site.register(UserProfile)
admin.site.register(Startup)
admin.site.register(Business)
