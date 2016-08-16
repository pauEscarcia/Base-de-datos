from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

#Direction
class Country(models.Model):
	clave= models.CharField(max_length=3)
	name= models.CharField(max_length=64)
	def __str__(self):
			return self.name

class Entity (models.Model):
	#cve_ent= models.CharField(max_length=2) primary key
	nam_ent= models.CharField(max_length=50)
	nam_abr= models.CharField(max_length=10)
	country_rel = models.ForeignKey(Country)
	def __str__(self):
		return self.nam_ent

class Municipality (models.Model):
	#cve_mun= models.CharField(max_length=3) primary Key
	nam_mun= models.CharField(max_length=50)
	cve_cab= models.CharField(max_length=4)
	nam_cab= models.CharField(max_length=50)
	entity_rel = models.ForeignKey(Entity)
	def __str__(self):
		return self.nam_mun

#--------------------------------------------------------------------------------

class Category(models.Model):
	idCategory = models.AutoField(primary_key=True)
	name= models.CharField(max_length=60)
	description= models.TextField()
#	def publish(self):
#		self.published_date = timezone.now()
#		self.save()

	def __str__(self):
		return self.name

class Clasification (models.Model):
	name= models.CharField(max_length=60)
	description= models.TextField()
	category_rel = models.ManyToManyField(Category)

	def __str__(self):
		return self.name
class Activity (models.Model):
	name= models.CharField(max_length=60)
	description= models.TextField()
	availability= models.CharField(max_length=60)
	duration= models.CharField(max_length=60)
	clasification_rel = models.ManyToManyField(Clasification)
	cost= models.TextField()
	currency= models.CharField(max_length=60)

	def __str__(self):
		return self.name
class Provider (models.Model):
	date = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=60)
	zip_code= models.CharField(max_length=6)
	address= models.CharField(max_length=60) 
	city_rel = models.ForeignKey(Entity)
	state_province_rel = models.ForeignKey(Municipality)
	country_rel = models.ForeignKey(Country)

	manager= models.CharField(max_length=60)
	email= models.EmailField()
	page= models.URLField()
	facebook= models.CharField(max_length=60, blank=True, null=True)
	youtube= models.CharField(max_length=60, blank=True, null=True)
	whatsapp= models.CharField(max_length=60, blank=True, null=True)
	instagram= models.CharField(max_length=60, blank=True, null=True)
	twitter= models.CharField(max_length=60, blank=True, null=True)
	tumblr= models.CharField(max_length=60, blank=True, null=True)
	business_phone= models.CharField(max_length=60)
	cel_phone= models.CharField(max_length=60, blank=True, null=True)
	latitude=models.FloatField()
	longitude=models.FloatField()
	activity_rel = models.ManyToManyField(Activity)

	def __str__(self):
		return self.name



