from django import template

register = template.Library()

@register.filter
def get(dictionary, key):
    return dictionary.get(key)

@register.filter
def to(value):
    return range(value)
