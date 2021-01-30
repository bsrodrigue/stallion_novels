from django.contrib import admin
from .models import Novel, Chapter, Like, Comment, Library

admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Library)
