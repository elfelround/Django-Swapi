from django import forms

from .models import Film


class FilmModelForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'


class SearchForm(forms.Form):
    name = forms.CharField(max_length=20)
