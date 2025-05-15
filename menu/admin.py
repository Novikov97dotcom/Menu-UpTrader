"""Admin interface for the menu app."""
from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Admin interface for MenuItem."""

    list_display = (
        'name', 'menu_name', 'url', 'named_url', 'parent', 'order'
    )
    list_filter = ('menu_name', 'parent')
    search_fields = ('name', 'menu_name', 'url', 'named_url')
    ordering = ('menu_name', 'order', 'name')
    list_editable = ('order',)
