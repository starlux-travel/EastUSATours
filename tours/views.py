from django.shortcuts import render
from django.http import HttpResponse  

def home(request):
    return render(request, 'home.html')

def search(request):
    departure = request.GET.get('departure')
    destination = request.GET.get('destination')
    print(f"出發地: {departure}, 目的地: {destination}")
    
    return render(request, 'search_results.html', {
        'departure': departure,
        'destination': destination,
    })