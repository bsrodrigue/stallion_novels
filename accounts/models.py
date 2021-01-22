from django.db import models
from django.contrib.auth.models import AbstractUser

class StallionUser(AbstractUser):
    is_writer = models.BooleanField(default=False)