from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect, HttpResponseBadRequest, request
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from django.views.generic.edit import DeleteView
from django.core.paginator import Paginator

from .models import Articolo, Categoria, Richiesta, User
from .forms import PostModelForm

class VisualizzaArticolo(ListView):
    queryset = Articolo.objects.all()
    template_name = "vetrina/lista_articoli.html"
    context_object_name = "lista_articoli"
    
def articolo_dettaglio(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    categoria_articolo = Categoria.objects.filter(
        articolo_appartenenza=articolo)
    context = {"articolo": articolo, "categoria": categoria_articolo}
    return render(request, "vetrina/articolo_dettaglio.html", context)

def categoria_visualizza(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    richiesta_categoria = Richiesta.objects.filter(categoria=categoria)
    form_richiesta = PostModelForm()
    context = {"categoria_v": categoria, 
               "form_richiesta": form_richiesta, 
               "richieste": richiesta_categoria}
    return render(request, "vetrina/categoria.html", context)

def aggiungi_richiesta(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.categoria = categoria
            form.instance.autore_richiesta = request.user
            form.save()
            url_categoria = reverse("view_categoria", kwargs={"pk": pk})
            return HttpResponseRedirect(url_categoria)
        else:
            return HttpResponseBadRequest()
        
          

class CancellaPost(DeleteView):
    model = Richiesta
    success_url = "/"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(autore_richiesta_id=self.request.user.id)	

	
 
