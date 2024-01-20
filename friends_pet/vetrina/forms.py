from django import forms

from .models import Domanda

class PostModelForm(forms.ModelForm):
		
	class Meta:
		model = Domanda
		fields = ["contenuto"]
		widgets = {
			"Tema" : forms.Textarea(attrs={'rows': '7'})
		}
		labels = {
			"contenuto" : "Inserisci la tua richiesta"
		}
