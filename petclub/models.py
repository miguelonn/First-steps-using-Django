import email
from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    rut = models.CharField(max_length=12)

    class Meta:
        managed = True



class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=1)
    color = models.CharField(max_length=50)
    class Meta:
        managed = True