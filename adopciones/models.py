from distutils.command.upload import upload
from django.db import models

class Adopciones(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre_mascota = models.CharField(max_length=200, verbose_name= 'Nombre de la Mascota')
    Edad = models.CharField(max_length=10, verbose_name='Edad')
    Porte = models.CharField(max_length=50, verbose_name= 'Porte')
    Raza = models.CharField(max_length=100, verbose_name='Raza')
    Imagen = models.ImageField(upload_to='imagenes/', null=True)                                        #instalar Pillow
    Datos_adicionales = models.CharField(max_length=300, verbose_name= 'Datos adicionales')
    Datos_persona = models.CharField(max_length=300, verbose_name= 'Datos de la persona')
    Direccion = models.CharField(max_length=300, verbose_name='Direccion')
    Telefono = models.CharField(max_length=10, verbose_name='Telefono')

    def __str__(self):        #visualizar datos en admin
        fila = "Nombre de la mascota" + self.Nombre_mascota + "-" +  "Raza" + self.Raza + "-" +  "Edad" + self.Edad
        return fila 

    def delete(self, using=None, keep_parents=False):    #borrar imagenes de admin y de la galeria proyecto
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()
