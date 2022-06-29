from atexit import register
from team.models import Members
from django import template

register = template.Library()

@register.inclusion_tag('presi.html')
def show_presi():
    presi = Members.objects.filter(designation = "President").order_by('batch_year').last()
    return{
        'presi' : presi
    }
