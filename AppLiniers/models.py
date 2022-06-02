from django.db import models

class Defensor (models.Model):
    nombre = models.CharField (max_length=15)
    apellido = models.CharField (max_length=15)
    edad = models.IntegerField ()
    puesto = models.IntegerField ()

class Medio (models.Model):
    nombre = models.CharField (max_length=15)
    apellido = models.CharField (max_length=15)
    edad = models.IntegerField ()
    puesto = models.IntegerField ()


class Delantero (models.Model):
    nombre = models.CharField (max_length=15)
    apellido = models.CharField (max_length=15)
    edad = models.IntegerField ()
    puesto = models.IntegerField ()
    