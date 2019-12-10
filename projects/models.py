from django.db import models

class ProjectArticle(models.Model):
	header = models.CharField(max_length=200, verbose_name='Название')
	image = models.ImageField(upload_to='project_images', verbose_name='Рисунок') 
	short_description = models.CharField(max_length=200, verbose_name='Краткое описание')
	text = models.TextField(verbose_name='Текст')

	def __str__ (self):
		return self.header

	class Meta():
		verbose_name = "Проект"
		verbose_name_plural = "Проекты"