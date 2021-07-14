from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image


class ProjectArticle(models.Model):
	header = models.TextField(verbose_name='Название')
	image = models.ImageField(upload_to='projects', blank=True, verbose_name='Рисунок') 
	short_description = models.TextField(verbose_name='Краткое описание')
	text = RichTextUploadingField(verbose_name='Текст')
	display = models.BooleanField(verbose_name='Показывать', default=True)

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