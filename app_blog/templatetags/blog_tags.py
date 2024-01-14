from django import template

register = template.Library()


@register.filter()
def media_path(val):
    if val:
        return f'/media/{val}'

    return '/static/image/blank_image.jpg'


@register.simple_tag()
def media_tag(value):
    if value:
        return f'/media/{value}'

    return '/static/image/blank_image.jpg'
