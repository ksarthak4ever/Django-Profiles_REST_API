from django.db import models
from django.contrib.auth.models import AbstractBaseUser #base of our user model
from django.contrib.auth.models import PermissionsMixin #to add permissions to users
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager): #It helps in teaching django how to use our new/custom UserProfile model
	
	def create_user(self,email,name,password=None): #creates a new user profile object.
		if not email:
			raise ValueError('Users must have an email address.')

		email = self.normalize_email(email) #to normalize entered email i.e all characters to lowercase 
		user = self.model(email=email, name=name)

		user.set_password(password) #set_password will encrypt the password in a hash
		user.save(using=self._db)

		return user

	def create_superuser(self,email,name,password): #to create and save a new superuser with given details
		user = self.create_user(email, name, password)
		user.is_superuser = True
		user.is_staff = True
		user.save(using = self._db)
		return user

		


class UserProfile(AbstractBaseUser, PermissionsMixin): #Used to represent a user profile inside our system or overwrite the existing user model made by django as in our api we want user to login through emails
	email = models.EmailField(max_length=200, unique=True)
	name = models.CharField(max_length=200)
	is_active = models.BooleanField(default=True) #to see if user is currently active in the system and is a requirement when creating custom user model
	is_staff = models.BooleanField(default=False) #also is required while substituting the built in user model

	objects = UserProfileManager() #used to help manage the user profiles i.e administrator user,regular user etc and also is required when substituting the built in user model.

	USERNAME_FIELD = 'email' #this field is used for login
	REQUIRED_FIELDS = ['name']

	def get_full_name(self): #to get a user full name by the django admin 
		return self.name

	def get_short_name(self):#used to get a users short name
		return self.name

	def __str__(self):#dunder or magic method used to convert the object to a string i.e convert it into human readable form
		return self.email



class ProfileFeedItem(models.Model): #profile status/feed update

	user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
	status_text = models.CharField(max_length=250)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self): #return the model as a string
		return self.status_text
