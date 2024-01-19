from django import forms

from .models import Categoria, Richiesta

class PostModelForm(forms.ModelForm):
		
	class Meta:
		model = Richiesta
		fields = ["contenuto"]
		widgets = {
			"Tema" : forms.Textarea(attrs={'rows': '7'})
		}
		labels = {
			"contenuto" : "Inserisci la tua richiesta"
		}
