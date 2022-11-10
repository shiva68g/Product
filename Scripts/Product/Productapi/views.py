from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import *
from .models import *
from .Serializer import *
from rest_framework.generics import ListAPIView


class Product(ListAPIView):
	queryset = productMainModel.objects.all()
	serializer_class = productMainModel_Serializer



class Product_With_id(APIView):

	get_queryset = productMainModel.objects
	
	def get(self , req , id):
		data = productMainModel.objects.filter(id=id)
		serializer = productMainModel_Serializer_with_Id(data , many=True)
		return Response(serializer.data)