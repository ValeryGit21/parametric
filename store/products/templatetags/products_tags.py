from django import template

from products.models import ProductsCategory


register = template.Library()


@register.simple_tag()
def tag_categories():
    return ProductsCategory.objects.all()
