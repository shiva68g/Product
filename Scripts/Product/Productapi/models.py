from django.db import models

# Create your models here.

# productMainModel

# Title
# Description
# Price
# unique_code(unique = true)
# Size = choice fields(10,20,30)
# Quality = choice fields(high,low,medium)

class productMainModel(models.Model):

	Size_choices = (
		('10' , '10'),
		('20' , '20'),
		('30' , '30'),
		)
	Quality_choices = (
		('high' , 'high'),
		('low' , 'low'),
		('medium' , 'medium')
		)

	Title = models.CharField(max_length=100)
	Description=models.TextField()
	Price = models.IntegerField()
	Unique = models.BooleanField()
	Size = models.CharField(max_length=100 , choices=Size_choices)
	Quality = models.CharField(max_length=100 , choices=Quality_choices)

	def __str__(self):
		return self.Title


# productColourModel

# Product = Fk
# Colour = choice fields(red,blue,green,black)

class productColourModel(models.Model):
	
	Colour_choices = (
		('black' , 'black'),
		('white' , 'white'),
		('blue' , 'blue'),
		('dark' , 'dark'),
		('red' , 'red')
		)
	Product = models.ForeignKey(productMainModel ,related_name='Colours', on_delete=models.CASCADE)
	Colour = models.CharField(max_length=100 , choices=Colour_choices)
	
	def __str__(self):
		return self.Colour


# productImageModel

# Product = Fk
# Image

class productImageModel(models.Model):
	Product = models.ForeignKey(productMainModel,related_name='Images', on_delete=models.CASCADE)
	Image = models.ImageField(upload_to="Images")