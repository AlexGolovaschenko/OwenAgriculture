from django.contrib import admin

from .models import ProductTopic, Product, TopicsGroup, ProductSpecification


class ProductSpecificationInline (admin.StackedInline):
	model = ProductSpecification

class ProductAdmin (admin.ModelAdmin):
	list_display = ['name', 'model', 'topic', 'used_in_poultry', 'used_in_pigsty']
	inlines = [ProductSpecificationInline]

class TopicsGroupAdmin (admin.ModelAdmin):
	list_display = ['headline', 'order']

class ProductTopicAdmin (admin.ModelAdmin):
	list_display = ['headline', 'order']

admin.site.register(ProductTopic, ProductTopicAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(TopicsGroup, TopicsGroupAdmin)