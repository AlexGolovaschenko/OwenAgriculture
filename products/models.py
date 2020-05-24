from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

class ProductTopic (models.Model):
	headline = models.CharField(verbose_name='Название', max_length=200)
	description = models.TextField(verbose_name='Описание')
	icon = models.ImageField(default='topic_icon_default.png', upload_to='topic_icons' )
	order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=0)

	def __str__ (self):
		return self.headline

	class Meta():
		verbose_name = "Категория продукта"
		verbose_name_plural = "Категории продуктов"


class Product (models.Model):
	topic = models.ForeignKey(ProductTopic, verbose_name='Категория продукта', on_delete=models.CASCADE)
	name = models.CharField(verbose_name='Полное наименование', max_length=100, blank=False)
	model = models.CharField(verbose_name='Модель', max_length=50, blank=False)
	image = models.ImageField(default='product_default.png', upload_to='products')
	short_description = models.TextField(verbose_name='Краткое описание', default='')
	order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=0)
	used_in_poultry = models.BooleanField(verbose_name='Используется в птицекомплексах', default=False)
	used_in_pigsty = models.BooleanField(verbose_name='Используется в свинокомплексах', default=False)

	def __str__ (self):
		return self.name

	class Meta():
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 600 or img.width > 600:
			output_size = (600, 600)
			img.thumbnail(output_size)
			img.save(self.image.path)


class ProductSpecificationField(models.Model):
	product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
	header = models.CharField(verbose_name='Оглавление', blank=False, max_length=50)
	specification = RichTextUploadingField (verbose_name='Описание', blank=False)
	order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=0)

	def __str__ (self):
		return 'Описание "%s" для %s' %(self.header, self.product.name)

	class Meta():
		verbose_name = "Раздел описания продукта"
		verbose_name_plural = "Разделы описания продукта"