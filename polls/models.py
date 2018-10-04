from django.db import models

# Create your models here.
class Imagen(models.Model):
    url = models.CharField(max_length=1000)