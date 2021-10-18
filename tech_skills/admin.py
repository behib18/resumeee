from tech_skills.models import TechSkills
from django.contrib import admin
from .models import TechSkills, OtherTechSkills


class Tech_SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill', 'quantity')
    list_display_links = ('skill', 'quantity')


admin.site.register(TechSkills, Tech_SkillsAdmin)


class OtherThechSkillsAdmin(admin.ModelAdmin):
    list_display = ('skill', )
    list_display_links = ('skill', )


admin.site.register(OtherTechSkills, OtherThechSkillsAdmin)
