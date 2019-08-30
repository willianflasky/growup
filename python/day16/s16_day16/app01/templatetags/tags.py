

from django import template
from django.utils.safestring import mark_safe

register = template.Library()   #register的名字是固定的,不可改变
@register.filter    #  只能接受两个参数
def mul(x,y):
    return x*y
@register.simple_tag
def mul2(x,y,z):
    return x*y*z

