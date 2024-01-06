from django.urls import path
from . import views

urlpatterns = [
	path('articoli/', views.Visualizza_articoli.as_view(), name='listart'),
	path('articolo/<int:pk>/', views.visualizza_articolo, name='articolo_view'),
]