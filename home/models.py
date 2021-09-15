from django.db import models
from django.utils import timezone
import main

class Produtora(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255, blank=True)
    logo_photo = models.ImageField(blank=True, upload_to='logos_empresas/%y/%m/%d/')

    def __str__(self):
                return self.name

class Games(models.Model):
    title = models.CharField(max_length=150)
    release = models.DateTimeField(default=timezone.now())
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=250)
    produtora = models.ForeignKey(Produtora, on_delete=models.DO_NOTHING)
    photo = models.ImageField(blank=True, upload_to='fotos/%y/%m/%d/')
    
    def __str__(self):
                return self.name

