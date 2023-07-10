from django import template

register = template.Library()


@register.filter()
def range_filter(star, end):
    return range(star, end + 1)
