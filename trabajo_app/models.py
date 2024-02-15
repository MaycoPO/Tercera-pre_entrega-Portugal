from django.db import models

# Create your models here.

class electrodomestico(models.Model):
    nombre = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)

class Cliente(models.Model):
    cliente = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

class Empleado(models.Model):
    empleado = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)