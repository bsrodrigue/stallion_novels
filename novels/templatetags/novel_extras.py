from django import template
register = template.Library()

from novels.models import Novel, Chapter, Like
from django.contrib.auth import get_user_model

@register.filter(name='is_my_novel')
def is_my_novel(novelId, userId):
    novel = Novel.objects.get(pk=novelId)
    author = novel.author
    return author.id == userId

@register.filter(name='novel_likes')
def novel_likes(novelId):
    novel = Novel.objects.get(pk=novelId)
    return novel.get_likes()

@register.filter(name='is_already_liked')
def is_already_liked(chapter_id, user_id):
    return Like.objects.filter(chapter=chapter_id, liker=user_id).exists()
