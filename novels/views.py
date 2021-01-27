from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Novel, Category, Chapter
from .forms import NovelCreationForm, ChapterCreationForm, ChapterEditForm

import readtime

def search(request):
    search_term = request.GET.get('search_term')
    found_novels = Novel.public_novels.filter(title__icontains=search_term).order_by("-created_at")
    return render(
        request,
        "novels/search_result.html",
        {
            "page_title": "Recherche",
            "found_novels": found_novels,
            "page_hero_title": "Résultats de recherche",
            "page_hero_description": "Lisez, écrivez et partagez des Webnovels Africains",
        },
    )

def edit_novel(request, novel_id):
    novel = Novel.objects.get(pk=novel_id)
    chapters = Chapter.objects.filter(novel=novel_id).order_by('created_at')

    return render(
        request,
        "novels/forms/edit_novel.html",
        {
            "page_title": f"{novel.title}",
            "novel": novel,
            "chapters": chapters,
            "page_hero_title": f"{novel.title}",
            "page_hero_description": f"{novel.description}",
        },
    )


def new_chapter(request, novel_id):
    if request.method == 'POST':
        form = ChapterCreationForm(request.POST)
        if form.is_valid():
            novel = Novel.objects.get(pk=novel_id)

            new_chapter = Chapter()
            new_chapter.title = form.cleaned_data['title']
            new_chapter.content = form.cleaned_data['content']
            new_chapter.novel = novel
            new_chapter.save()

            return HttpResponseRedirect(reverse_lazy('my_creations'))
    return render(request, 'novels/forms/new_chapter.html')

def edit_chapter(request, chapter_id):
    if request.method == 'POST':
        form = ChapterEditForm(request.POST)
        if form.is_valid():

            edited_chapter = Chapter.objects.get(pk=chapter_id)
            edited_chapter.title = form.cleaned_data['title']
            edited_chapter.content = form.cleaned_data['content']
            edited_chapter.save()

            return HttpResponseRedirect(reverse_lazy('my_creations'))

    chapter_to_be_edited = Chapter.objects.get(pk=chapter_id)
    return render(request, 'novels/forms/edit_chapter.html', {
        'chapter_id': chapter_id,
        'chapter': chapter_to_be_edited,
    })

def delete_chapter(request, chapter_id):
    chapter_to_be_deleted = Chapter.objects.get(pk=chapter_id)
    chapter_to_be_deleted.delete()
    return HttpResponseRedirect(reverse_lazy('my_creations'))

def delete_novel(request, novel_id):
    novel_to_be_deleted = Novel.objects.get(pk=novel_id)
    novel_to_be_deleted.delete()
    return HttpResponseRedirect(reverse_lazy('my_creations'))

def create_novel(request):
    if request.method == 'POST':
        form = NovelCreationForm(request.POST)
        if form.is_valid():

            new_novel = Novel()
            new_novel.title = form.cleaned_data['title']
            new_novel.description = form.cleaned_data['description']
            new_novel.author = request.user
            new_novel.category = Category.objects.get(pk=1)

            new_novel.save()

            return HttpResponseRedirect(reverse_lazy('my_creations'))
    else:
        form = NovelCreationForm()

    return render(request, 'novels/forms/new_novel.html', {'form': form})


def my_creations(request):
    latest_novels = Novel.objects.order_by("-created_at")
    my_created_novels = Novel.objects.filter(author=request.user.id)
    return render(
        request,
        "novels/my_creations.html",
        {
            "page_title": "Mes Créations",
            "my_created_novels": my_created_novels,
            "page_hero_title": "Mes créations",
            "page_hero_description": "",
        },
    )


def home(request):
    latest_novels = Novel.public_novels.order_by("-created_at")
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
    latest_novels = Novel.objects.filter(
        category=category_id).order_by("-created_at")
    return render(
        request,
        "novels/category.html",
        {
            "page_title": f"Catégorie {category.title}",
            "latest_novels": latest_novels,
            "page_hero_title": f"{category.title}",
            "page_hero_description": f"{category.description}",
        },
    )


def chapter(request, novel_id, chapter_index):
    novel = Novel.objects.get(pk=novel_id)
    chapters = Chapter.objects.filter(novel=novel_id).order_by('created_at')

    paginator = Paginator(chapters, 1)

    page_number = request.GET.get('page')
    target_page_number = page_number or chapter_index

    page_obj = paginator.get_page(target_page_number)
    current_chapter = page_obj[0]
    reading_time = readtime.of_html(current_chapter.content)

    return render(
        request,
        "novels/chapter.html",
        {
            "page_title": f"{current_chapter.title}",
            "novel": novel,
            "chapters": chapters,
            "page_obj": page_obj,
            "current_chapter": current_chapter,
            "reading_time": reading_time.minutes,
            "page_hero_title": f"Chapitre: {current_chapter.title}",
            "page_hero_description": f"Bonne lecture",
        },
    )


def novel(request, novel_id):
    novel = Novel.objects.get(pk=novel_id)
    chapters = Chapter.objects.filter(novel=novel_id).order_by('created_at')

    return render(
        request,
        "novels/novel.html",
        {
            "page_title": f"{novel.title}",
            "novel": novel,
            "chapters": chapters,
            "page_hero_title": f"{novel.title}",
            "page_hero_description": f"{novel.description}",
        },
    )
