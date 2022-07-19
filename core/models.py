from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Service(models.Model):
	title= models.CharField(max_length=250)
	description= models.CharField(max_length=250)
	content= RichTextField()

	def __str__(self):
		return self.title

class Team(models.Model):
	name = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
	qualification = models.CharField(max_length=100,null=True,blank=True)
	description = models.TextField(max_length=250,blank=True,null=True)
	image = models.ImageField(null=True,blank=True)

	def __str__(self):
		return str(self.name + self.role)

class Message(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=70)
	phone = models.CharField(max_length=20,null=True,blank=True)
	message = models.TextField(max_length=300)
	sent_at = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.message