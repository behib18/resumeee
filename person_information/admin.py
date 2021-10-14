from django.contrib import admin

from .models import PersonInfo


class Person_infornationAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthday', 'website', 'phone', 'degree')
    list_display_links = ('user', 'birthday', 'website', 'phone', 'degree')
    # make sure that admin can not enter more than 1 record!

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(PersonInfo, Person_infornationAdmin)
