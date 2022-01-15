from django.db import models

# Create your models here.

class Entries(models.Model):
	API=models.CharField(max_length=100)
	Description=models.CharField(max_length=100)
	Auth=models.CharField(max_length=100,blank=True)
	HTTP=models.BooleanField(default=False)
	Cors=models.CharField(max_length=10)
	Link=models.CharField(max_length=200)
	Category=models.CharField(max_length=100)


	def __str__(self):
		return self.API