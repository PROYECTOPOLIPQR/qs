from django.db import models

class Solicitud(models.Model):
    nombres = models.CharField(max_length=150, verbose_name='Nombres')
    apellidos = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='No')
    archivo = models.FileField(upload_to='documents/%Y/%m/%d', null=True)
    observaciones = models.CharField(max_length=350, blank=True, null=True )
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)