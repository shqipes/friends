from django.shortcuts import render
from .models import Articolo

# Create your views here.
def articolo(request):
    articoli = Articolo.objects.all()
    context ={"articoli": articoli}
    return render(request, "gallery/articoli_lista.html", context)
