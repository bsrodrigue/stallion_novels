from django import forms
from djrichtextfield.widgets import RichTextWidget

from .models import Novel

class NovelForm(forms.Form):
    title = forms.CharField(label='Titre', max_length=100)
    description = forms.CharField(label='Description')
    genre = forms.ChoiceField(choices=Novel.GENRES)


class ChapterForm(forms.Form):
    title = forms.CharField(label='Titre', max_length=100)
    content = forms.CharField(label='Contenu')
    public = forms.BooleanField(label='Rendre public', required=False)
