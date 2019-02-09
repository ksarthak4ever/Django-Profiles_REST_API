from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response


class HelloApiView(APIView):
	""" Testing API View. """

	def get(self,request,format=None):
		"Returns a list of APIView features."

		an_apiview = [
			'Hello',
			'World',
			'Testing',
			'ksarthak4ever'
		]

		return Response({'message': 'Hello!', 'an_apiview': an_apiview})


