from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Novel, Category


def home(request):
    latest_novels = Novel.objects.order_by('-created_at')
    return render(
        request,
        "novels/home.html",
        {
            "page_title": "Stallion Novels",
            "latest_novels": latest_novels,
            "page_hero_title": "Bienvenue sur Stallion Novels",
            "page_hero_description": "Lisez, écrivez et partagez des Webnovels Africains",
        },
    )


def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    category_novels = Novel.objects.filter(category=category_id).order_by('-created_at')
    return render(
        request,
        "novels/category.html",
        {
            "page_title": f"Catégorie {category.title}",
            "category_novels": category_novels,
            "page_hero_title": f"Catégorie {category.title}",
            "page_hero_description": f"Catégorie {category.description}",
        }
    )