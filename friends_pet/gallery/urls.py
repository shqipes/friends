from django.urls import path
from . import views

urlpatterns = [
	path('articoli', views.articolo, name='listart'),
	
]