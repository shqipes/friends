from django.urls import path
from . import views

urlpatterns = [
	path('articoli/', views.VisualizzaArticolo.as_view(), name='view_art'),
	
	path('articolo/<int:pk>/', views.articolo_dettaglio, name='articolo_view'),
	path('categoria/<int:pk>/', views.categoria_visualizza, name='view_categoria'),
 	path('categoria/<int:pk>/rispondi/', views.aggiungi_richiesta, name="richiesta_articolo"),
  	path("categoria/<int:id>/elimina-post/<int:pk>/", views.CancellaPost.as_view(), name="cancella_post"),
]	