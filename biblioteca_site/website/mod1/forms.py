from django import forms
from django.forms import ModelForm, fields
from .models import Libro

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['ISBN', 'nombreLibro', 'autorLibro', 'descLibro', 'categoriaLibro']