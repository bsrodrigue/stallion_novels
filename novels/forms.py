from django import forms
from djrichtextfield.widgets import RichTextWidget

class NovelCreationForm(forms.Form):
    title = forms.CharField(label='Titre', max_length=100)
    description = forms.CharField(label='Description', max_length=1000)

class ChapterCreationForm(forms.Form):
    title = forms.CharField(label='Titre', max_length=100)
    content = forms.CharField(label='Contenu',widget=RichTextWidget())
