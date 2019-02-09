from django.contrib import admin
from . import models

admin.site.register(models.UserProfile) #from admin.site module importing register function and passing our UserProfile model