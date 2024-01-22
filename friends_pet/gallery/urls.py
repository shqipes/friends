from django.urls import path
from . import views

urlpatterns = [
	path('articoli/', views.Visualizza_articoli.as_view(), name='listart'),
 	path('staff', views.Visualizza_Galleria_staff.as_view(), name='lista_staf'),
	path('nuovo-articolo/', views.Aggiungi_articolo.as_view(), name="add_art"),
	path("elimina/<int:pk>/", views.Cancella_articolo.as_view(), name="del_art"),
]