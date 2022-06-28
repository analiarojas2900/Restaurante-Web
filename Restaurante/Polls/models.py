from django.db import models
from pyexpat import model
from tabnanny import verbose

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id Categorias')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre Categorias')

    def __str__(self):
        return self.nombreCategoria

class Comida(models.Model):
    idPlato = models.AutoField( primary_key=True, verbose_name='Id Plato')
    precio = models.CharField(max_length=10, verbose_name='Precio')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    img=models.ImageField(upload_to = 'Polls/static/Polls/img/',null=True,verbose_name='Imagen')
    caracteristica = models.CharField(max_length=20,null=True, blank=True, verbose_name='Caracteristica')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.idPlato


class Usuario(models.Model):
    usuarioN= models.CharField(max_length=30,verbose_name="Nombre de Usuario")
    passwordN= models.CharField(max_length=15, verbose_name="Contraseña")
    password2N=models.CharField(max_length=15, verbose_name=" Contraseña2")