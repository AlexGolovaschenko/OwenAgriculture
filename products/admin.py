from django.contrib import admin

from .models import ProductTopic, Product, TopicsGroup

admin.site.register(ProductTopic)
admin.site.register(Product)
admin.site.register(TopicsGroup)