from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=300)
    image = models.CharField(max_length=200)
    
class User(models.Model):
    pass