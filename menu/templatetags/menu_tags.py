"""Template tags for the menu app."""
from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """Render a tree-like menu structure by menu name."""

    request = context['request']
    current_url = request.path
    menu_items = MenuItem.objects.filter(
        menu_name=menu_name
    ).select_related('parent')
    active_item = None
    for item in menu_items:
        if item.get_url() == current_url:
            active_item = item
            break
    active_ancestors = []
    if active_item:
        active_ancestors = active_item.get_ancestors()
    root_items = [item for item in menu_items if item.parent is None]
    return {
        'menu_items': root_items,
        'active_item': active_item,
        'active_ancestors': active_ancestors,
    } 