from django.db import models


class ProductTopic (models.Model):
	headline = models.CharField(max_length=200)
	description = models.TextField()

	def __str__ (self):
		return self.headline


class Product (models.Model):
	topic = models.ForeignKey(ProductTopic, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __str__ (self):
		return self.name