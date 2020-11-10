from django.db import models

class Solicitud(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombres', blank=True )
    email = models.CharField(max_length=150, verbose_name='Correo', blank=True )
    phone = models.CharField(max_length=10, unique=True, verbose_name='Telefono', blank=True )
    message = models.CharField(max_length=350, blank=True )    
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)