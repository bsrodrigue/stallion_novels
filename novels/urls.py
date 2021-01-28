from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('genre/<str:genre_name>', views.genre, name='genre'),
    path('search', views.search, name='search'),
    path('novel/<int:novel_id>', views.novel, name='novel'),
    path('chapter/<int:novel_id>/<int:chapter_index>',
         views.chapter, name='chapter'),
]


# Account Related
urlpatterns += [
    path('account/my_creations', views.my_creations, name='my_creations'),
    path('preview_chapter/<int:novel_id>/<int:chapter_index>',
         views.preview_chapter, name='preview_chapter'),
    path('account/novel_dashboard/<int:novel_id>',
         views.novel_dashboard, name='novel_dashboard'),
]

# Novel
urlpatterns += [
    path('account/new_novel', views.new_novel, name='new_novel'),
    path('account/edit_novel/<int:novel_id>', views.edit_novel, name='edit_novel'),
    path('account/delete_novel/<int:novel_id>',
         views.delete_novel, name='delete_novel'),
]

# Chapter
urlpatterns += [
    path('account/new_chapter/<int:novel_id>',
         views.new_chapter, name='new_chapter'),
    path('account/edit_chapter/<int:chapter_id>',
         views.edit_chapter, name='edit_chapter'),
    path('account/delete_chapter/<int:chapter_id>',
         views.delete_chapter, name='delete_chapter'),
]
