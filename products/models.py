from pickle import TRUE
from django.db import models

class Products(models.Model):
    nombres = models.CharField(max_length=30,blank=False)
    apellido = models.CharField(max_length=15)
    f_nacimiento = models.CharField(max_length=10)
    sexo = models.CharField(max_length=30,null=True, blank=True)
    edad = models.CharField(max_length=30,null=True, blank=True)
    altura = models.FloatField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    creation_date = models. DateField(auto_now_add=True)
    
