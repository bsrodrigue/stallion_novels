from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    reads = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)

    novel = models.ForeignKey(
        'Novel',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

class Novel(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    cover = models.ImageField(upload_to='novel_covers')
    reads = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    adult = models.BooleanField(default=False)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def has_chapters(self):
        chapters = Chapter.objects.filter(novel=self)
        return len(chapters)

    def __str__(self):
        return self.title

