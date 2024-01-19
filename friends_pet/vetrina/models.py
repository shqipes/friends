from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articolo(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.ImageField()
    codart = models.CharField(max_length=8)
    descrizione = models.TextField()
    prezzo = models.FloatField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"
        
    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    titolo = models.CharField(max_length=40)
    data_categoria = models.DateField(auto_now_add=True)
    dettagli = models.TextField()
    articolo_appartenenza = models.ForeignKey(Articolo, on_delete=models.CASCADE, related_name="categorie")
    
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorie"
        
    def __str__(self):
        return self.titolo
    
class Richiesta(models.Model):
    autore_richiesta = models.ForeignKey(User, on_delete=models.CASCADE, related_name="richieste")
    data_richiesta = models.DateField(auto_now_add=True)
    contenuto = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="richieste")
    
    class Meta:
        verbose_name = "Richiesta"
        verbose_name_plural = "Richieste"
        
    def __str__(self):
        return self.autore_richiesta.username
    
