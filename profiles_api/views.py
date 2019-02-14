from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status #status contains list of different http response status codes(e.g. http404, http505 etc.)
from rest_framework.authentication import TokenAuthentication #gives user a temporary token that inserts in the headers of the http request, drs then uses this token to check if user has authenticated with the system
from rest_framework import filters # to add search functionality to the api
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken #These two are used to trick drs into using its login api view as viewsets so we can use our standard default router.By making LoginApi as a viewset we can add it to the api root
from rest_framework.permissions import IsAuthenticatedOrReadOnly # so one wont be able to create new object/feed unless they are logged in in the system but still be able to see already posted feeds
from rest_framework.permissions import IsAuthenticated #so only registered users can see other users feeds and post feeds

from . import serializers
from . import models
from . import permissions



class HelloApiView(APIView): 
	""" Testing API View. """

	serializer_class = serializers.HelloSerializer #telling django what serializer to use to describe the data that we handle with this api view.serializer_class is the variable/object used here to connect.

	def get(self, request, format=None): #http get method.returns the data passed.
		
		an_apiview = [
			'Hello',
			'World',
			'Testing',
			'ksarthak4ever'
		]

		return Response({'message': 'Hello!', 'an_apiview': an_apiview})


	def post(self, request): #http post method.Creates hello message with our names

		serializer = serializers.HelloSerializer(data=request.data) #as request object of post method stores the data we posted(i.e request made to the api) so we are passing that data here so our serializer knows which data to base our serializer on.

		if serializer.is_valid(): #checking if data passed in the serializer is valid
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name) #using proper python string notation i.e if more that one message passes then store the order in which we want the string to go
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, pk=None): #handles updating an object
		return Response({'method': 'put'})


	def patch(self, request, pk=None): #patch request,only updates fields provided in the request
		return Response({'method': 'patch'})


	def delete(self, request, pk=None): #deletes an object
		return Response({'method': 'delete'})


class HelloViewSet(viewsets.ViewSet):
	""" Testing API Viewset """

	serializer_class = serializers.HelloSerializer

	def list (self,	request): #used to return a hello message and creating an index for all other viweset operations
		
		a_viewset = [
			'Testing basic CRUD functions',
			'i.e Create,Read,Update,Delete',
			'ksarthak4ever'
		]

		return Response({'message': 'Hello!', 'a_viewset': a_viewset})


	def create(self, request):

		serializer = serializers.HelloSerializer(data=request.data) #passing data to the serializer

		if serializer.is_valid(): #checking if data passed in the serializer is valid
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name) 
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		


	def retrieve(self, request, pk=None): #handles getting an object by its id
		return Response({'http_method': 'GET'})


	def update(self, request, pk=None): #used for updating an object
		return Response({'http_method': 'PUT'})


	def partial_update(self, request, pk=None): #to update part of an object
		return Response({'http_method': 'PATCH'})


	def destroy(self, request, pk=None): #to remove an object
		return Response({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet): #Handles creating,reading and updating profiles.ModelViewSet of djangorestframework takes care of all the logic for creating,reading and updating model items(really useful for simple apis)

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all() #queryset tells the viewset how to retrieve the objects from database i,e from which model.
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,) #added , to create them as tupples as we can use multiple authentication classes or permission classes for e.g. we can also use SessionAuthentication
	filter_backends	= (filters.SearchFilter,)
	search_fields = ('name', 'email',) #which fields we wanna allow the user to filter by, as told in the documentation



class LoginViewSet(viewsets.ViewSet): #checks email and password and returns an auth token. We could have used standard
	
	serializer_class = AuthTokenSerializer

	def create(self, request): #uses the ObtainAuthToken APIView to validate and create a token. create fn is called during http POST request
		return ObtainAuthToken().post(request) #same as calling ObtainAuthToken normally here we are just calling it through our ViewSet and returning the response in the create fn.



class UserProfileFeedViewSet(viewsets.ModelViewSet): #Handles creating,reading and updating profile feed items.

	authentication_classes = (TokenAuthentication,)
	serializer_class = serializers.ProfileFeedItemSerializer
	queryset = models.ProfileFeedItem.objects.all()
	permission_classes = (permissions.PostOwnStatus, IsAuthenticated)

	def perform_create(self, serializer): #sets the user profile to the logged in user. As in DRS when a new obejct is created we have to manually set the the object to the user profile currently logged in.
		serializer.save(user_profile=self.request.user)
