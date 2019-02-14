''' Serializer object in django rest framework is used to describe the data that we need to return or retrieve from our api.
 Basically converts a text string of json into a python object and vice versa '''

from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer): #serializes a name field for testing our APIView
	name = serializers.CharField(max_length=10) #as django serializers also have a lot of predefined validations in their fields etc.



class UserProfileSerializer(serializers.ModelSerializer): #A serializer for user profile objects, importing ModelSerializer to use its features
	
	class Meta:
		model = models.UserProfile #this tells the django rest framework that ModelSerializer is gonna be used with our UserProfile model
		fields = ('id', 'email', 'name', 'password') #passing the fields we wanna use in the serializer
		extra_kwargs = {'password': {'write_only': True}} #adding special keyword argument/attribute to the desired fields,so password wont be displayed

	def create(self, validated_data): # To create and return a new User.Special function used to overwrite the create functionality as we wanna be in control of how the users are created.
		user = models.UserProfile(
				email = validated_data['email'],
				name = validated_data['name']
			)
		user.set_password(validated_data['password'])
		user.save()
		return user



class ProfileFeedItemSerializer(serializers.ModelSerializer): #A serializer for profile feed items.

	class Meta:
		model = models.ProfileFeedItem
		fields = ('id', 'user_profile', 'status_text', 'created_on')
		extra_kwargs = {'user_profile': {'read_only': True}} #as we want to set this automatically based on the user thats automatically logged in as we dont want user to create someone else's feed items
