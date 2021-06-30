from rest_framework import serializers
from mod1.models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['ISBN', 'nombreLibro', 'autorLibro', 'descLibro', 'categoriaLibro']
