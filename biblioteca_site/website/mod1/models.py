from django.db import models

# Create your models here.
#categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de la Categoria")

    def __str__(self):
        return self.nombreCategoria


#libros
class Libro(models.Model):
    ISBN = models.IntegerField(primary_key=True, verbose_name= "ISBN-10")
    nombreLibro = models.CharField(max_length=50, verbose_name="Nombre del libro")
    autorLibro = models.CharField(max_length=60,verbose_name= "Autor del libro")
    descLibro = models.CharField(max_length=1000, verbose_name= "Descripcion del libro")
    categoriaLibro = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __parseInt__(self):
        return self.ISBN


    #traer datos
    



