from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessaggioModelForm

# Create your views here.
def contatto_view(request):
    if request.method == "POST":
        form = MessaggioModelForm(request.POST)
        if form.is_valid():
            nuovo_messaggio = form.save()
            return HttpResponse ("<h1>Grazie per averci contattato!<h1>")
    else:
        form = MessaggioModelForm()
    context = {"form": form}
    return render(request, "contatto/form_contatto.html", context)
     