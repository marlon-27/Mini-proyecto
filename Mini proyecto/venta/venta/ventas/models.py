from django.db import models

# Create your models here.

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.CharField(max_length=40)
    def __str__(self):
        return self.nombre
    


class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    cedula = models.CharField(max_length=40)
    producto = models.ForeignKey(Productos, on_delete =models.CASCADE)
    


class descripcion(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion

    
    def __str__(self):
        return self.nombre

    def __str__(self):
        return self.descripcion