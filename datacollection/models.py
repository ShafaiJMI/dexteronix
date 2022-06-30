from django.db import models

# Create your models here.
class Dustbin(models.Model):
	dustbinid = models.CharField(max_length=100)
	location = models.CharField(max_length=150,null=True,blank=True)
	level = models.IntegerField(default=0)
	added_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.dustbinid