from django.contrib import admin
from .models import Banner

class BannerAdmin (admin.ModelAdmin):
	list_display = ['name', 'order', 'display']

admin.site.register(Banner, BannerAdmin)
