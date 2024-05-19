from django.contrib import admin
from django.utils.html import format_html

from vendor.models import Vendor


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'seller_type', 'vendor_url')
    list_display_links = ('id', 'name', 'seller_type')
    list_filter = ('seller_type', 'contacts__city')
    actions = ['make_published']

    def contacts_city(self, obj):
        return obj.contacts.city

    def vendor_url(self, obj):
        if obj.vendor:
            return format_html("<a href='{url}'>{name}</a>",
                               url=obj.vendor.id, name=obj.vendor.name)
        return "N/A"

    vendor_url.short_description = "Ссылка на подрядчика"

    @admin.action(description="Списание задолженности")
    def make_published(self, request, queryset) -> None:
        queryset.update(debt=0)
