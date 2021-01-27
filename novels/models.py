from django.db import models
from djrichtextfield.models import RichTextField
from django.contrib.auth import get_user_model

from .managers import PublicNovelsManager

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    created_at = models.DateField(auto_now_add=True)
    publication_date = models.DateField(blank=True, null=True)
    reads = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)
    public = models.BooleanField(default=False)

    novel = models.ForeignKey(
        'Novel',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.novel}:{self.title}"

class Novel(models.Model):
    GENRES = [
        ("UNKNOWN", "Inconnu"),
        ("FANTASY", "Fantasy"),
        ("ADVENTURE", "Aventure"),
        ("ROMANCE", "Romance"),
    ]
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    cover = models.ImageField(upload_to='novel_covers', default='novel_covers/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    publication_date = models.DateField(blank=True, null=True)
    mature = models.BooleanField(default=False)
    public = models.BooleanField(default=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    genre = models.CharField(choices=GENRES, max_length=30, default="F")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    objects = models.Manager()
    public_novels = PublicNovelsManager()
    

    def get_chapters(self):
        chapters = Chapter.objects.filter(novel=self).order_by('-created_at')
        return chapters

    def __str__(self):
        return self.title

