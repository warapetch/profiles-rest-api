from django.contrib import admin
from profiles_api import models


admin.site.register(models.UserProfile)     #1
admin.site.register(models.ProfileFeedItem) #2
