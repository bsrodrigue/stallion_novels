from django import template
register = template.Library()

from novels.models import Novel
from django.contrib.auth import get_user_model

@register.filter(name='is_my_novel')
def is_my_novel(novelId, userId):
    novel = Novel.objects.get(pk=novelId)
    author = novel.author
    return author.id == userId

