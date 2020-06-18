from django.db import models

class File (models.Model):
	name = models.CharField(verbose_name='Наименование', max_length=100, blank=False)
	file = models.FileField(verbose_name='Файл', upload_to='filestorage/%Y/%m/%d/', blank=False)

	class Meta:
		verbose_name = 'Документ'
		verbose_name_plural = 'Документы'

