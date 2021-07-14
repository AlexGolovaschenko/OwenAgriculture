from django.contrib import admin

from .models import ProjectArticle



class ProjectAdmin (admin.ModelAdmin):
	list_display = ['header', 'display']
    list_editable = ['display']

admin.site.register(ProjectArticle, ProjectAdmin)

