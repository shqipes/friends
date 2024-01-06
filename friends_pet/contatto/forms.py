from django import forms
from .models import Messaggio

class MessaggioModelForm(forms.ModelForm):
    
    class Meta:
        model = Messaggio
        fields = "__all__"