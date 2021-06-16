
from .forms import LibroForm
from django.shortcuts import render, redirect
from django.template import loader
from .models import Libro
# Create your views here.

def home(request):
    return render(request, 'mod1/home.html')

def libros(request):
    libros = Libro.objects.all()
    datos = {
        'libros': libros
    }

    return render(request, 'mod1/libros.html', datos)


def form_libros(request):
    datos = {
        'form': LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos Guardados Correctamente"

    return render(request, 'mod1/form_libros.html', datos)    


def form_mod(request, id):
    libro = Libro.objects.get(ISBN=id)
    datos = {
        'form' : LibroForm(instance=libro)

    }
    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, instance=libro)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificacion correctamente"
    
    return render(request, 'mod1/form_mod.html', datos)


def form_eli(request, id):
    libro = Libro.objects.get(ISBN=id)
    libro.delete()
    return redirect(to="libros")

def formulario(request):
    return render(request, 'mod1/formulario.html')



    
