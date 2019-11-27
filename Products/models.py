from django.db import models


class ProductTopic (models.Model):
	headline = models.CharField(max_length=200)
	description = models.TextField()

	def __str__ (self):
		return self.headline


class Product (models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	topic = models.ForeignKey(ProductTopic, on_delete=models.CASCADE)

	def __str__ (self):
		return self.name