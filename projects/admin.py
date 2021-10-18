from django.contrib import admin
from .models import Project, Photo


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    list_display_links = ('name', 'title')


admin.site.register(Project, ProjectsAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', )
    list_display_links = ('id', )


admin.site.register(Photo, PhotoAdmin)
