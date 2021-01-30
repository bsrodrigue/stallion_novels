from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from novels.models import Novel

class StallionUser(AbstractUser):
    library = models.ManyToManyField(Novel, blank=True)