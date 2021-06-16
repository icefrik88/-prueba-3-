from django.urls import path
from .views import form_libros, home, form_mod, libros, form_eli

urlpatterns = [
    path('', home, name='home'),
    path('libros.html', libros, name='libros'),
    path('form_libros.html', form_libros, name='form_libros'),
    path('from-mod/<id>', form_mod, name='form_mod'),
    path('from-eli/<id>', form_eli, name='form_eli'),

    
]
