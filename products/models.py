from django.db import models
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


class TopicsGroup (models.Model):
	headline = models.CharField(verbose_name='Название', max_length=200)
	order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=0)
	topics = models.ManyToManyField(ProductTopic, verbose_name='Категории продуктов')

	def __str__ (self):
		return self.headline

	class Meta():
		verbose_name = "Группа"
		verbose_name_plural = "Группы"


class Product (models.Model):
	topic = models.ForeignKey(ProductTopic, verbose_name='Категория продукта', on_delete=models.CASCADE)
	name = models.CharField(verbose_name='Полное наименование', max_length=100, blank=False)
	model = models.CharField(verbose_name='Модель', max_length=50, blank=False)
	image = models.ImageField(default='product_default.png', upload_to='product_pictures')
	short_description = models.CharField(verbose_name='Краткое описание', max_length=200, default='')
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


class ProductSpecification (models.Model):
	product = models.OneToOneField(
	        Product,
	        on_delete=models.CASCADE,
	        primary_key=True,
	    )
	description = models.TextField(verbose_name='Описание', blank=True)
	specifications = models.TextField(verbose_name='Технические характеристики', blank=True) # should be table
	func_scheme = models.ImageField(verbose_name='Функциональная схема', upload_to='product_schemes', blank=True)
	сontrols_description = models.TextField(verbose_name='Элементы управления', blank=True)
	dimensions = models.TextField(verbose_name='Габаритные размеры', blank=True) # should be table
	connection_scheme = models.ImageField(verbose_name='Cхемы подключения', upload_to='product_schemes', blank=True) # can be many images (OneToMany ????)
	documentation = models.TextField(verbose_name='Документация', blank=True) # should be html template with lincs for download file
	package_bundle = models.TextField(verbose_name='Комплектация', blank=True)

	def __str__ (self):
		return 'Specification ' + self.product.name

	class Meta():
		verbose_name = "Спецификация продукта"
		verbose_name_plural = "Спецификации продуктов"