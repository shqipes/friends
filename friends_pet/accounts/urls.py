from django.urls import path
from .views import registrazione_views

urlpatterns = [
	path("registrazione/", registrazione_views, name="registration_view"),
 	
]