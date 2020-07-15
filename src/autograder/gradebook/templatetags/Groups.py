from django import template
from django.contrib.auth.models import Group

#This file exists to check if a user is part of a specific group
register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False