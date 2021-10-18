from django.contrib import admin
from .models import ContactForm, Contact

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('your_name', 'subject')
    list_display_links = ('your_name', 'subject')
admin.site.register(ContactForm, ContactFormAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('description',)
    list_display_links = ('description',)
    # make sure that admin can not enter more than 1 record!

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(Contact, ContactAdmin)
