from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"
        
        
class Articolo(models.Model):
    foto = models.ImageField()
    nome = models.CharField(max_length=25)
    cod_art = models.CharField(max_length=6, blank=True, null=True)
    descrizione = models.TextField()
    prezzo = models.FloatField()
    
    
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"
        
    def get_absolute_url(self):
        return reverse("listart", kwargs={"pk": self.pk})
    
    
    