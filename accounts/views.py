# accounts/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")

@login_required
def profile(request):
    return render(request, "accounts/profile.html")

@login_required
def orders(request):
    return render(request, "accounts/orders.html")
