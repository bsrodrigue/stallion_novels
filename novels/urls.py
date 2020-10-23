from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('category/<int:category_id>', views.category, name='category'),
    path('novel/<int:novel_id>', views.novel, name='novel'),
    path('chapter/<int:novel_id>/<int:chapter_index>', views.chapter, name='chapter')
]
