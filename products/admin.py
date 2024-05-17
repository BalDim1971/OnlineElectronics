from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'date_release')
    list_display_links = ('id', 'name')
    list_filter = ('name',)
    ordering = ['date_release']
