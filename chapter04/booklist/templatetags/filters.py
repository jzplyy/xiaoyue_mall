import datetime

from django import template

register = template.Library()


# def sum(value, arg):
#     return value + arg
#
#
# register.filter('sum', sum)


# @register.filter(name='examp')
# def examp(value, arg):
#     return value + arg
#

# @register.filter
# def examp(value, arg):
#     return value + arg


def get_current_time(timezone, format_string):
    return datetime.datetime.now(timezone).strftime(format_string)


@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    timezone = context['timezone']
    # get_current_time()是自定义的获取当前时间的方法
    return get_current_time(timezone, format_string)


