from django.urls import path

from .views import contatto_view

urlpatterns = [
   path('contattaci/', contatto_view, name='contact_view'),
   
]