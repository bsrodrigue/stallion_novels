from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Novel, Chapter, Like
from .forms import NovelForm, ChapterForm

import readtime

def unlike_chapter(request, chapter_id):
    like_to_delete = Like.objects.filter(chapter=chapter_id, liker=request.user.id)[0]
    like_to_delete.delete()
    return HttpResponseRedirect(reverse_lazy('home'))


def like_chapter(request, chapter_id):
    chapter = Chapter.objects.get(pk=chapter_id)

    new_like = Like()
    new_like.liker = request.user
    new_like.chapter = chapter
    new_like.save()

    return HttpResponseRedirect(reverse_lazy('home'))


def search(request):
    search_term = request.GET.get('search_term')
    found_novels = Novel.public_novels.filter(
        title__icontains=search_term).order_by("-created_at")
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


def novel_dashboard(request, novel_id):
    novel = Novel.objects.get(pk=novel_id)
    chapters = Chapter.objects.filter(novel=novel_id).order_by('created_at')

    return render(
        request,
        "novels/novel_dashboard.html",
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
        form = ChapterForm(request.POST)
        if form.is_valid():
            novel = Novel.objects.get(pk=novel_id)

            new_chapter = Chapter()
            new_chapter.title = form.cleaned_data['title']
            new_chapter.content = form.cleaned_data['content']
            new_chapter.novel = novel
            new_chapter.public = form.cleaned_data['public']
            new_chapter.save()

            return HttpResponseRedirect(reverse_lazy('my_creations'))
        else:
            return HttpResponse('Formulaire invalide')


    return render(request, 'novels/forms/chapter_form.html', {
        'novel_id': novel_id,
        'new_chapter': 'new_chapter',

    })


def edit_chapter(request, chapter_id):
    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            edited_chapter = Chapter.objects.get(pk=chapter_id)
            edited_chapter.title = form.cleaned_data['title']
            edited_chapter.content = form.cleaned_data['content']
            edited_chapter.public = form.cleaned_data['public']
            edited_chapter.save()

            return HttpResponseRedirect(reverse_lazy('my_creations'))
        else:
            return HttpResponse('Formulaire invalide')


    chapter_to_be_edited = Chapter.objects.get(pk=chapter_id)
    return render(request, 'novels/forms/chapter_form.html', {
        'chapter_id': chapter_id,
        'chapter': chapter_to_be_edited,
        'edit_chapter': 'edit_chapter',

    })


def delete_chapter(request, chapter_id):
    chapter_to_be_deleted = Chapter.objects.get(pk=chapter_id)
    chapter_to_be_deleted.delete()
    return HttpResponseRedirect(reverse_lazy('my_creations'))


def delete_novel(request, novel_id):
    novel_to_be_deleted = Novel.objects.get(pk=novel_id)
    novel_to_be_deleted.delete()
    return HttpResponseRedirect(reverse_lazy('my_creations'))


def edit_novel(request, novel_id):
    if request.method == 'POST':
        genres_mapping = {
            'Inconnu': 'Inconnu',
            'Fantasy': 'Fantasy',
            'Aventure': 'Aventure',
            'Romance': 'Romance',
        }
        form = NovelForm(request.POST)
        if form.is_valid():

            novel_to_be_edited = Novel.objects.get(pk=novel_id)
            novel_to_be_edited.title = form.cleaned_data['title']
            novel_to_be_edited.description = form.cleaned_data['description']
            novel_to_be_edited.genre = genres_mapping[form.cleaned_data['genre']]

            novel_to_be_edited.save()

            return HttpResponseRedirect(reverse_lazy('my_creations'))


    novel_to_be_edited = Novel.objects.get(pk=novel_id)
    form = NovelForm(initial={
        'genre': novel_to_be_edited.genre,
    })
    
    return render(request, 'novels/forms/novel_form.html',{
        'form': form,
        'edit_novel': 'edit_novel',
        'novel': novel_to_be_edited,
        })


def new_novel(request):
    if request.method == 'POST':
        genres_mapping = {
            'Inconnu': 'Inconnu',
            'Fantasy': 'Fantasy',
            'Aventure': 'Aventure',
            'Romance': 'Romance',
        }
        form = NovelForm(request.POST)
        if form.is_valid():

            new_novel = Novel()
            new_novel.title = form.cleaned_data['title']
            new_novel.description = form.cleaned_data['description']
            new_novel.author = request.user
            new_novel.genre = genres_mapping[form.cleaned_data['genre']]

            new_novel.save()

            return HttpResponseRedirect(reverse_lazy('my_creations'))
        else:
            print(form.errors)
    else:
        form = NovelForm()

    return render(request, 'novels/forms/novel_form.html',{
        'form': form,
        'new_novel': 'new_novel',
        })


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


def genre(request, genre_name):
    genres_mapping = {
        'Inconnu': ['Inconnu', 'Plongez dans des univers fantastiques où votre imagination est la seule limite.'],
        'Fantasy': ['Fantasy', 'Plongez dans des univers fantastiques où votre imagination est la seule limite.'],
        'Aventure': ['Aventure', 'Échappez à la routine et vivez de grandes aventures.'],
        'Romance': ['Romance', 'Vous croyez en l\'amour? Laissez votre coeur s\'emballer avec notre collection d\'histoires roses.'],
    }
    requested_genre = genres_mapping[genre_name]

    requested_genre_novels = Novel.objects.filter(
        genre=genre_name).order_by("-created_at")
    return render(
        request,
        "novels/genre.html",
        {
            "page_title": f"Genre {requested_genre[0]}",
            "requested_genre_novels": requested_genre_novels,
            "page_hero_title": f"Collection {requested_genre[0]}",
            "page_hero_description": f"{requested_genre[1]}",
        },
    )


def preview_chapter(request, novel_id, chapter_index):
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
            "page_hero_title": f"{current_chapter.title}",
            "page_hero_description": f"Bonne lecture",
        },
    )


def chapter(request, novel_id, chapter_index):
    novel = Novel.objects.get(pk=novel_id)
    chapters = Chapter.objects.filter(novel=novel_id, public=True).order_by('created_at')

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
            "page_hero_title": f"{current_chapter.title}",
            "page_hero_description": f"Bonne lecture",
        },
    )


def novel(request, novel_id):
    novel = Novel.objects.get(pk=novel_id)
    chapters = Chapter.objects.filter(novel=novel_id, public=True).order_by('created_at')

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
