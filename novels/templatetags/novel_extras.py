from django import template
register = template.Library()

from novels.models import Novel, Chapter, Like, Library
from django.contrib.auth import get_user_model


@register.filter(name='is_already_in_library')
def is_already_in_library(novelId, userId):
    # novel = Novel.objects.get(pk=novelId)
    library = Library.objects.filter(owner=userId)[0]
    return library.novels.filter(pk=novelId).exists()

@register.filter(name='is_my_novel')
def is_my_novel(novelId, userId):
    novel = Novel.objects.get(pk=novelId)
    author = novel.author
    return author.id == userId

@register.filter(name='novel_likes')
def novel_likes(novelId):
    novel = Novel.objects.get(pk=novelId)
    return novel.get_likes()

@register.filter(name='chapter_likes')
def chapter_likes(chapter_id):
    chapter = Chapter.objects.get(pk=chapter_id)
    return chapter.get_likes()

@register.filter(name='chapter_comments')
def chapter_comments(chapter_id):
    chapter = Chapter.objects.get(pk=chapter_id)
    return chapter.get_comments().count()

@register.filter(name='novel_public_chapters')
def novel_public_chapters(novelId):
    novel = Novel.objects.get(pk=novelId)
    return novel.get_public_chapters().count()

@register.filter(name='novel_comments')
def novel_comments(novelId):
    novel = Novel.objects.get(pk=novelId)
    return novel.get_comment_count()

@register.filter(name='is_already_liked')
def is_already_liked(chapter_id, user_id):
    return Like.objects.filter(chapter=chapter_id, liker=user_id).exists()
