from django.db import models

# Create your models here.
class Banner (models.Model):
	name = models.CharField(verbose_name='Название', max_length=100, blank=False)
	banner_image = models.ImageField(verbose_name='Картинка баннера', upload_to='banners', blank=False)
	order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=0)
	display = models.BooleanField(verbose_name='Показывать', default=True)

	def __str__ (self):
		return self.name

	class Meta():
		verbose_name = "Баннер"
		verbose_name_plural = "Баннеры"

