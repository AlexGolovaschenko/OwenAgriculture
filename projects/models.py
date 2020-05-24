from django.db import models
from PIL import Image


class ProjectArticle(models.Model):
	header = models.CharField(max_length=200, verbose_name='Название')
	image = models.ImageField(upload_to='projects', blank=True, verbose_name='Рисунок') 
	short_description = models.CharField(max_length=200, verbose_name='Краткое описание')
	text = models.TextField(verbose_name='Текст')

	def __str__ (self):
		return self.header

	class Meta():
		verbose_name = "Проект"
		verbose_name_plural = "Проекты"

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 600 or img.width > 600:
			output_size = (600, 600)
			img.thumbnail(output_size)
			img.save(self.image.path)