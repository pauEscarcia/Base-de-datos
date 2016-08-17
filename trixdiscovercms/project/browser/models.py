from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

#Direction
class Country(models.Model):
	key= models.CharField(max_length=3)
	name= models.CharField(max_length=64)
	def __str__(self):
			return self.name

#entidad
class State (models.Model):
	#cve_ent= models.CharField(max_length=2) primary key
	nam_sta= models.CharField(max_length=50)
	nam_abr= models.CharField(max_length=10)
	country_rel = models.ForeignKey(Country)
	def __str__(self):
		return self.nam_sta

#municipio
class City (models.Model):
	#cve_mun= models.CharField(max_length=3) primary Key
	nam_city= models.CharField(max_length=50)
	cve_cab= models.CharField(max_length=4)
	nam_cab= models.CharField(max_length=50)
	entity_rel = models.ForeignKey(State)
	def __str__(self):
		return self.nam_city

#--------------------------------------------------------------------------------

class Images(models.Model):
	location= models.CharField(max_length=255)
	title= models.CharField(max_length=64)
	def __str__(self):
			return self.title
#--------------------------------------------------------------------------------

class Category(models.Model):
	idCategory = models.AutoField(primary_key=True)
	name= models.CharField(max_length=60)
	description= models.TextField()
	def __str__(self):
		return self.name

class Classification (models.Model):
	name= models.CharField(max_length=60)
	description= models.TextField()
	category_rel = models.ManyToManyField(Category)
	def __str__(self):
		return self.name

class Activity (models.Model):
	status= models.CharField(max_length=60, null=True)
	name= models.CharField(max_length=60)
	description= models.TextField()
	availability= models.CharField(max_length=60)
	duration= models.CharField(max_length=60)
	classification_rel = models.ManyToManyField(Classification)
	images_rel = models.ManyToManyField(Images)
	cost= models.TextField()
	currency= models.CharField(max_length=60)
	def __str__(self):
		return self.name

class Provider (models.Model):
	status= models.CharField(max_length=60, null=True)
	date = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=60)
	zip_code= models.CharField(max_length=6)
	address= models.CharField(max_length=60) 

	city_rel = models.ForeignKey(City)
	state_province_rel = models.ForeignKey(State)
	country_rel = models.ForeignKey(Country)

	manager= models.CharField(max_length=60)
	email= models.EmailField()
	page= models.URLField()
	facebook= models.URLField(null=True)
	youtube= models.URLField(null=True)
	whatsapp= models.CharField(max_length=60, blank=True, null=True)
	instagram= models.CharField(max_length=60, blank=True, null=True)
	twitter= models.CharField(max_length=60, blank=True, null=True)
	#tumblr= models.CharField(max_length=60, blank=True, null=True)
	business_phone= models.CharField(max_length=60)
	cel_phone= models.CharField(max_length=60, blank=True, null=True)
	latitude=models.FloatField()
	longitude=models.FloatField()
	activity_rel = models.ManyToManyField(Activity)
	def __str__(self):
		return self.name



