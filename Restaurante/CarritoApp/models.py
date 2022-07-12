from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    img=models.ImageField(upload_to = 'Polls/static/Polls/img/',null=True,verbose_name='Imagen')
    caracteristica = models.TextField(max_length=200,null=True, blank=True, verbose_name='Caracteristica')
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
