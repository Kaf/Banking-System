from django.db import models
from django.contrib import admin

# Create your models here.
class Person(models.Model):
	name: models.CharField(max_length=50)
	dob: models.DateField()
	phone: models.PositiveIntegerField()
	address: models.TextField()
	email: models.EmailField(required=True)
	accnum: models.PositiveIntegerField()
	created: models.DateTimeField(auto_now_add=True)
	def __unicode__():
		return self.name
