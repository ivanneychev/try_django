from django.shortcuts import render


def home(request):
    return render(request, 'restaurants/home.html')


def about(request):
    return render(request, 'restaurants/about.html')
