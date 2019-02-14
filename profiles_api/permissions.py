'''
Permission checks are always run at the very start of the view, before any other code is allowed to proceed. Permission checks will typically use the authentication information in the request.user and request.auth properties to determine if the incoming request should be permitted.

Permissions are used to grant or deny access different classes of users to different parts of the API.

Documentations :~ https://www.django-rest-framework.org/api-guide/permissions/
 '''

from rest_framework import permissions  #permissions module contain all the base permissions classes in djangorestframework 


class UpdateOwnProfile(permissions.BasePermission): #allows users to edit their own profile.

	def has_object_permission(self, request, view, obj): #this fn runs every time a request is made to the api and it checks if user is trying to update his own class or not i.e has permission or not by returning a simple true or false

 		if request.method in permissions.SAFE_METHODS: #as we want users to be able to view any profile in the system and dont wanna apply any permission on that by checking the SAFE_METHODS list.A safe method is a non destructive method i.e allows one to retrieve data but does'nt allow to change.modify or delete any objects in the system e.g http GET
 			return True

 		return obj.id == request.user.id #checking if the user is trying to update his own profile i.e the object he is trying to update has the same id as the current authenticated user.



class PostOwnStatus(permissions.BasePermission): #allows users to update only their own feeds/status.

 	def has_object_permission(self, request, view, obj): #checks the user is trying to update his own status

 		if request.method in permissions.SAFE_METHODS:
 			return True

 		return obj.user_profile.id == request.user.id