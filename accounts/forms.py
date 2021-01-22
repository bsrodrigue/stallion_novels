from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import StallionUser


class StallionUserCreationForm(UserCreationForm):
    class Meta:
        model = StallionUser
        fields = ('username', 'email')


class StallionUserChangeForm(UserChangeForm):
    class Meta:
        model = StallionUser
        fields = ('username', 'email')
