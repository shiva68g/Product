from rest_framework import serializers
from .models import *


class productColourModel_Serializer(serializers.ModelSerializer):
	class Meta:
		model = productColourModel
		fields = '__all__'




class productImageModel_Serializer(serializers.ModelSerializer):
	class Meta:
		model = productImageModel
		fields = '__all__'



# Title
# Description
# Price
# unique_code(unique = true)
# Size = choice fields(10,20,30)
# Quality = choice fields(high,low,medium)

class productMainModel_Serializer(serializers.ModelSerializer):
	Colours = serializers.StringRelatedField(many=True , read_only=True)
	Images = serializers.StringRelatedField(many=True , read_only=True)
	class Meta:
		model = productMainModel
		fields = ['Title' , 'Description' ,
		 'Price' , 'Unique' , 'Size' ,
		  'Quality' , 'Colours' , 'Images']


class productMainModel_Serializer_with_Id(serializers.ModelSerializer):
	Colours = serializers.StringRelatedField(many=True , read_only=True)
	Images = serializers.StringRelatedField(many=True , read_only=True)
	class Meta:
		model = productMainModel
		fields = '__all__'