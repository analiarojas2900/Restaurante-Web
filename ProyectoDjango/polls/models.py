from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id de categoría')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre de la categpria')

    def __str__(self):
        return self.nombreCategoria

class Comida(models.Model):
    precio = models.CharField(max_length=6,primary_key=True, verbose_name='Precio')
    plato = models.CharField(max_length=20, verbose_name='Plato')
    tipo = models.CharField(max_length=20,null=True, blank=True, verbose_name='Tipo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.precio