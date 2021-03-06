from django.contrib import admin

from .models import Article

class NewsAdmin (admin.ModelAdmin):
    list_display = ['header', 'display', 'pub_date']
    list_editable = ['display']

admin.site.register(Article, NewsAdmin)

