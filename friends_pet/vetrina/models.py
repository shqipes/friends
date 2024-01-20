from django.db import models
from django.contrib.auth.models import User

    # nuovo database
class Oggetto(models.Model):
    nome = models.CharField(max_length=50)
    foto = models.ImageField()
    codart = models.CharField(max_length=8)
    descrizione = models.TextField()
    prezzo = models.FloatField()
    
    class Meta:
        verbose_name = "Oggetto"
        verbose_name_plural = "Oggetti"
    
    def __str__(self):
        return self.nome
    
class Tipologia(models.Model):
    titolo = models.CharField(max_length=50)
    data_tipologia = models.DateField(auto_now_add=True)
    dettagli = models.TextField()
    oggetto_appartenenza = models.ForeignKey(Oggetto, on_delete=models.CASCADE, related_name="tipologie")
    
    class Meta:
        verbose_name = "Tipologia"
        verbose_name_plural = "Tipologie"
        
    def __str__(self):
        return self.titolo
    
class Domanda(models.Model):
    autore_domanda = models.ForeignKey(User, on_delete=models.CASCADE, related_name="domande")
    data_domanda = models.DateField(auto_now_add=True)
    contenuto = models.TextField()
    tipologia_appartenenza = models.ForeignKey(Tipologia, on_delete=models.CASCADE, related_name="domande")
    oggetto_appartenenza = models.ForeignKey(Oggetto, on_delete=models.CASCADE, related_name="domande")
    
    class Meta:
        verbose_name = "Domanda"
        verbose_name_plural = "Domande"
        
    def __str__(self):
        return self.autore_domanda.username
    


    
    
