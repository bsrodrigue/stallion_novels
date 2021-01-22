from django import forms

class NovelCreationForm(forms.Form):
    title = forms.CharField(label='Titre', max_length=100)
    description = forms.CharField(label='Déscription', max_length=1000)