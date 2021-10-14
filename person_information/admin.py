from django.contrib import admin

from .models import PersonInfo


class Person_infornationAdmin(admin.ModelAdmin):
    # make sure that admin can not enter more than 1 record!
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(PersonInfo, Person_infornationAdmin)
