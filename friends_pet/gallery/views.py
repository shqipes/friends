from django.shortcuts import render, get_object_or_404
from .models import Articolo
from django.views.generic.list import ListView

# Create your views here.
class Visualizza_articoli(ListView):
    queryset = Articolo.objects.all()
    template_name = "gallery/articoli_lista.html"
    context_object_name = "lista_articoli"




def visualizza_articolo(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "gallery/descrizione_art.html", context)