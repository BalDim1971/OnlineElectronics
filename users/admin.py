from django.contrib import admin
from users.models import User


@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'email',
                    'first_name',
                    'last_name',
                    'is_active',
                    )
    list_display_links = ('id', 'email')
    list_filter = ('email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)
