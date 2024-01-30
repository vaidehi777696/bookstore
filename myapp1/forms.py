from django import forms
from .models import Booksavailable


class BooksavailableForm(forms.ModelForm):
    class Meta:
        model=Booksavailable
        fields=['bookname','authorname']