import random
from django import template
register = template.Library()

@register.filter
def randomshuffle(arg):
    tmp = list(arg)[:]
    random.shuffle(tmp)
    return tmp