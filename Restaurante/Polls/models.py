from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id Categorias')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre Categorias')

    def __str__(self):
        return self.nombreCategoria

class Comida(models.Model):
    idPlato = models.CharField(max_length=6, primary_key=True, verbose_name='Id Plato')
    precio = models.CharField(max_length=10, verbose_name='Precio')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    caracteristica = models.CharField(max_length=20,null=True, blank=True, verbose_name='Caracteristica')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.idPlato