from django.db import models
from django.urls import reverse

# Create your models here.
        
class Articolo(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=25, blank=True, null=True)
    cod_art = models.CharField(max_length=6, blank=True, null=True)
    descrizione = models.TextField(blank=True, null=True)
    prezzo = models.FloatField(blank=True, null=True)
    
    
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"
        
    def get_absolute_url(self):
        return reverse("listart", kwargs={"pk": self.pk})
    