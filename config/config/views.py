# config/config/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Landing page - available to anyone

def home(request):
    return render(request, 'registration/home.html')

# Optional: a dashboard page for logged-in users
@login_required
def dashboard(request):
    return render(request, 'registeration/.html')