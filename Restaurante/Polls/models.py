from django.db import models

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


class Usuarios(models.Model):
    usrN= models.CharField(max_length=30,verbose_name="Nombre de Usuario")
    pswrdN= models.CharField(max_length=15, verbose_name="Contraseña")
    pswrdN2=models.CharField(max_length=15, verbose_name="Contraseña2")
#fin modelos para usuarios

#se crea modelo de token
class Tokens(models.Model):
    token= models.CharField(max_length=256)
    user = models.CharField(max_length=256)