from atexit import register
from team.models import Members
from django import template

register = template.Library()

@register.inclusion_tag('presi.html')
def show_presi():
    presi = Members.objects.filter(designation = "President")
    if presi.count()>0 :
        presi = presi.reverse()[0]
    else :
        presi = None
    return{
        'presi' : presi
    }
