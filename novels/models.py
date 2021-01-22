from django.db import models
from djrichtextfield.models import RichTextField
from django.contrib.auth import get_user_model

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    created_at = models.DateField(auto_now_add=True)
    reads = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)

    novel = models.ForeignKey(
        'Novel',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.novel}:{self.title}"

class Novel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    cover = models.ImageField(upload_to='novel_covers', default='novel_covers/ln-cover-1.jpg')
    reads = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    adult = models.BooleanField(default=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def get_chapters(self):
        chapters = Chapter.objects.filter(novel=self).order_by('-created_at')
        return chapters

    def __str__(self):
        return self.title

