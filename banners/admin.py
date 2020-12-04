from django.contrib import admin
from .models import Banner

class BannerAdmin (admin.ModelAdmin):
	list_display = ['name', 'banner_image', 'display', 'order']

admin.site.register(Banner, BannerAdmin)