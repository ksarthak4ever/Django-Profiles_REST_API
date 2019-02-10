''' Serializer object in django rest framework is used to describe the data that we need to return or retrieve from our api.
 Basically converts a text string of json into a python object and vice versa '''

from rest_framework import serializers


class HelloSerializer(serializers.Serializer): #serializes a name field for testing our APIView
	name = serializers.CharField(max_length=10) #as django serializers also have a lot of predefined validations in their fields etc.