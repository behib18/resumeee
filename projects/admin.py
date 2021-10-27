from django.contrib import admin
from .models import Project, Photo, Video


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    list_display_links = ('name', 'title')


admin.site.register(Project, ProjectsAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', )
    list_display_links = ('image', )


admin.site.register(Photo)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('caption', )
    list_display_links = ('caption', )


admin.site.register(Video, VideoAdmin)
