from django.db import models

class Article(models.Model):
	header = models.CharField(max_length=200, verbose_name='Название')
	image = models.ImageField(upload_to='news_images', blank=True, verbose_name='Рисунок')
	short_description = models.CharField(max_length=200, verbose_name='Краткое описание')	 
	text = models.TextField(verbose_name='Текст')

	def __str__ (self):
		return self.header

	class Meta():
		verbose_name = "Новость"
		verbose_name_plural = "Новости"