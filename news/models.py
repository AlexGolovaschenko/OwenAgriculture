from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
from PIL import Image

class Article(models.Model):
	header = models.TextField(verbose_name='Название')
	image = models.ImageField(upload_to='news', blank=True, verbose_name='Рисунок')
	short_description = models.TextField(verbose_name='Краткое описание')	 
	text = RichTextUploadingField(verbose_name='Текст')
	pub_date = models.DateField(verbose_name='Дата публикации', default=datetime.date.today)

	def __str__ (self):
		return self.header

	class Meta():
		verbose_name = "Новость"
		verbose_name_plural = "Новости"

	def save(self):
		super().save()
		if self.image:
			img = Image.open(self.image.path)
			if img.height > 600 or img.width > 600:
				output_size = (600, 600)
				img.thumbnail(output_size)
				img.save(self.image.path)