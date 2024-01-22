from django.urls import path

from .views import HomeView, user_profile_view, staff_home

urlpatterns = [
    path("", HomeView, name="homepage"),
    path("staff/", staff_home, name="staffhome"),
    path('user/<str:username>/', user_profile_view, name="user_profile"),     
 ]