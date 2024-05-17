from django.contrib import admin

from contacts.models import Contacts


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'city', 'street', 'house')
    list_display_links = ('id', 'email')
    list_filter = ('email',)
    ordering = ['country']
