from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('category/<int:category_id>', views.category, name='category'),
]
