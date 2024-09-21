from django import template

register = template.Library()

@register.filter
def length_is(value, length):
    """Check if the length of value is equal to length."""
    return len(value) == length
