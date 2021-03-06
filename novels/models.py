from django.db import models
from djrichtextfield.models import RichTextField
from django.contrib.auth import get_user_model
import stallion_novels.settings as settings

from .managers import PublicNovelsManager

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"User '{self.author.username}' commented Chapter '{self.chapter.title}' from Novel '{self.chapter.novel.title}'"


class Like(models.Model):
    liker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    chapter = models.ForeignKey(
        'Chapter', on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.liker.username} likes {self.chapter.title} from {self.chapter.novel.title}"


class Chapter(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    publication_date = models.DateField(blank=True, null=True)
    reads = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)
    public = models.BooleanField(default=False)

    novel = models.ForeignKey(
        'Novel',
        on_delete=models.CASCADE,
    )

    def get_likes(self):
        likes = Like.objects.filter(chapter=self)
        return likes.count()

    def get_comments(self):
        comments = Comment.objects.filter(chapter=self)
        return comments

    def __str__(self):
        return f"{self.novel}:{self.title}"


class Novel(models.Model):
    GENRES = [
        ("Inconnu", "Inconnu"),
        ("Fantasy", "Fantasy"),
        ("Aventure", "Aventure"),
        ("Romance", "Romance"),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='novel_covers',
                              default='novel_covers/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateField(blank=True, null=True)
    mature = models.BooleanField(default=False)
    public = models.BooleanField(default=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    genre = models.CharField(choices=GENRES, max_length=30, default="Inconnu")
    objects = models.Manager()
    public_novels = PublicNovelsManager()

    def get_chapters(self):
        chapters = Chapter.objects.filter(novel=self).order_by('-created_at')
        return chapters

    def get_public_chapters(self):
        chapters = Chapter.objects.filter(public=True, novel=self)
        return chapters

    def get_likes(self):
        chapters = self.get_chapters()
        likes = 0
        for chapter in chapters:
            likes += chapter.get_likes()
        return likes

    def get_comment_count(self):
        chapters = self.get_chapters()
        comments = 0
        for chapter in chapters:
            comments += chapter.get_comments().count()
        return comments

    def __str__(self):
        return self.title
