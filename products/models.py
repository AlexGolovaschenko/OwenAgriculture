from django.db import models


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
	name = models.CharField(verbose_name='Наименование', max_length=100, default='')
	image = models.ImageField(default='product_default.png', upload_to='product_pictures')
	short_description = models.CharField(verbose_name='Краткое описание', max_length=200, default='')
	description = models.TextField(verbose_name='Полное описание', default='')
	used_in_poultry = models.BooleanField(verbose_name='Используется в птицекомплексах', default=False)
	used_in_pigsty = models.BooleanField(verbose_name='Используется в свинокомплексах', default=False)

	def __str__ (self):
		return self.name

	class Meta():
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"


class TopicsGroup (models.Model):
	hedline = models.CharField(verbose_name='Название', max_length=200)
	order = models.PositiveSmallIntegerField(verbose_name='Порядок отображения', default=0)
	topics = models.ManyToManyField(ProductTopic, verbose_name='Категории продуктов')

	def __str__ (self):
		return self.hedline

	class Meta():
		verbose_name = "Группа"
		verbose_name_plural = "Группы"
