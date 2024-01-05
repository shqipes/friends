from django.urls import path

from .views import HomeView, user_profile_view

urlpatterns = [
    path("", HomeView, name="homepage"),
    path('user/<str:username>/', user_profile_view, name="user_profile"),     
 ]