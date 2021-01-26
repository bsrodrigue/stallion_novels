from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>', views.category, name='category'),
    path('novel/<int:novel_id>', views.novel, name='novel'),
    path('chapter/<int:novel_id>/<int:chapter_index>',
         views.chapter, name='chapter'),
]


# Account Related
urlpatterns += [
    path('account/my_creations', views.my_creations, name='my_creations'),
    path('account/create_novel', views.create_novel, name='create_novel'),
    path('account/edit_novel/<int:novel_id>', views.edit_novel, name='edit_novel'),
    path('account/new_chapter/<int:novel_id>', views.new_chapter, name='new_chapter'),
]
