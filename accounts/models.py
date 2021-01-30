from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# class StallionUserManager(BaseUserManager):
#     def create_user(self, username, password=None):
#         if not username:
#             raise ValueError('Users must have a username')
#         user = self.model(username=username)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, username, password=None):
#         if not username:
#             raise ValueError('Users must have a username')
#         user = self.model(username=username)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user


class StallionUser(AbstractUser):
    pass