from django import template

register = template.Library()

@register.filter
def my_filter(data):
    return data + ' - ' + 'Alterado pelo filter'
