from django import forms

from .models import (
    Film,
    People,
    PeopleImage,
)


class FilmModelForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'


class PeopleModelForm(forms.ModelForm):
    class Meta:
        model = People
        fields = '__all__'


class PeopleImageModelForm(forms.ModelForm):
    class Meta:
        model = PeopleImage
        fields = '__all__'
