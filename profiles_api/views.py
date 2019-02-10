from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status #status contains list of different http response status codes(e.g. http404, http505 etc.)

from . import serializers



class HelloApiView(APIView): # Testing API View.

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





