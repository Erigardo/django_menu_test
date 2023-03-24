from django import template
from menu_test.models import MenuItem

register = template.Library()

@register.simple_tag()
def draw_menu(menu_test):
    menu_items = MenuItem.objects.filter(parent=None, menu=menu_test).select_related('parent')

    current_url = context['request'].path
    for item in menu_items:
        item.is_active = current_url.startswith(item.url)

    if item.is_active:
        parent = item.parent
        while parent is not None:
            parent.is_expanded = True
            parent = parent.parent

    return {'menu_items': menu_items}

