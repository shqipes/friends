from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView

from django.contrib.auth.models import User
# Create your views here.

def HomeView(request):
    return render(request, "core/homepage.html")

def user_profile_view(request, username):
    user = get_object_or_404(User, username=username)
    context = {"user": user}
    return render(request, 'core/user_profile.html', context)