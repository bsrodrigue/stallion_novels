from django.contrib import admin
from .models import Novel, Chapter, Like

admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(Like)
