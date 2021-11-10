from django.contrib import admin
from .models import Licence, Language, Background, Experience, Summary, Education


class SummaryAdmin(admin.ModelAdmin):
    list_display = ('description',)
    list_display_links = ('description',)
    pass


admin.site.register(Summary, SummaryAdmin)


class Background_infoAdmin(admin.ModelAdmin):
    list_display = ('description',)
    list_display_links = ('description',)

    # make sure that admin can not enter more than 1 record!
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(Background, Background_infoAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'institute_name', 'description')
    list_display_links = ('title', 'institute_name', 'description')


admin.site.register(Education, EducationAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_display_links = ('title', 'description')


admin.site.register(Experience, ExperienceAdmin)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('title', 'level')
    list_display_links = ('title', 'level')


admin.site.register(Language, LanguageAdmin)


class LicenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')
    list_display_links = ('title', 'year')


admin.site.register(Licence, LicenceAdmin)
