from django.db import models

# Create your models here.
class FastFood(models.Model):
    name=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    ffimg=models.URLField()

class Chinese(models.Model):
    name=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    cimg=models.URLField()

class SouthIndian(models.Model):
    name=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    simg=models.URLField()