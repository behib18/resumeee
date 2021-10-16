from education.models import Education
from django.contrib import admin

class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'institute_name', 'description')
    list_display_links = ('title', 'institute_name', 'description')

admin.site.register(Education, EducationAdmin)
