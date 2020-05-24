from django.contrib import admin

from .models import ProductTopic, Product, ProductSpecificationField


class ProductSpecificationInline (admin.StackedInline):
	model = ProductSpecificationField
	extra = 0

class ProductAdmin (admin.ModelAdmin):
	list_display = ['name', 'model', 'topic', 'used_in_poultry', 'used_in_pigsty']
	inlines = [ProductSpecificationInline]

class ProductTopicAdmin (admin.ModelAdmin):
	list_display = ['headline', 'order']

admin.site.register(ProductTopic, ProductTopicAdmin)
admin.site.register(Product, ProductAdmin)
