from django.db import models

class PublicNovelsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(public=True)
