from django.shortcuts import render

def home(request): return render(request, 'movies/home.html')
def now_showing(request): return render(request, 'movies/now_showing.html')
def details(request): return render(request, 'movies/details.html')
def login_view(request): return render(request, 'movies/login.html')
def theatres(request): return render(request, 'movies/theaters.html')