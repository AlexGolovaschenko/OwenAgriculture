from django.db import models


class ProductTopic (models.Model):
	headline = models.CharField(verbose_name='Название', max_length=200)
	description = models.TextField(verbose_name='Описание')
	order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=0)

	def __str__ (self):
		return self.headline

	class Meta():
		verbose_name = "Категория продукта"
		verbose_name_plural = "Категории продуктов"


class Product (models.Model):
	topic = models.ForeignKey(ProductTopic, verbose_name='Категория продукта', on_delete=models.CASCADE)
	name = models.CharField(verbose_name='Наименование', max_length=200)
	description = models.TextField(verbose_name='Описание')

	def __str__ (self):
		return self.name

	class Meta():
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"