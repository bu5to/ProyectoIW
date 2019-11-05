from django.db import models

# Create your models here.

class Marca(models.Model):
    id = models.CharField(max_length = 5, primary_key =True)
    nombre = models.CharField(max_length = 20)
    desc = models.TextField()
    logo = models.ImageField()


    def __init__(self):
        return self.nombre


class Ropa(models.Model):
    id = models.CharField(max_length = 10, primary_key =True)
    nombre = models.CharField(max_length = 30)
    tipo = models.CharField(max_length = 120)
    pvp = models.DecimalField(max_digits = 7, decimal_places = 2)
    pfinal = models.DecimalField(max_digits = 7, decimal_places = 2, default = pvp)
    categoria = models.CharField(max_length = 120)
    desc = models.TextField()
    img = models.ImageField()
    marca = models.ForeignKey('Marca', on_delete = models.CASCADE)


    """docstring for Ropa."""
    def __init__(self):
        return self.nombre
