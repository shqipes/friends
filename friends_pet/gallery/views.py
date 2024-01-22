from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .mixins import StaffMixing
from .models import Articolo
# Create your views here.
class Visualizza_articoli(ListView):
    queryset = Articolo.objects.all()
    template_name = "gallery/articoli_lista.html"
    context_object_name = "lista_articoli"

class Visualizza_Galleria_staff(StaffMixing, ListView):
    queryset = Articolo.objects.all()
    template_name = "gallery/articoli_lista_staf.html"
    context_object_name = "lista_staf"

class Aggiungi_articolo(StaffMixing, CreateView):
    model = Articolo
    fields = "__all__"
    template_name = "gallery/aggiungi_art.html"
    success_url = reverse_lazy ('lista_staf')
    
class Cancella_articolo(StaffMixing, DeleteView):
    model = Articolo
     
    success_url = reverse_lazy ('lista_staf')
    
    


