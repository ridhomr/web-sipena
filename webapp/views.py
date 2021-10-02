from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def about(request):
    context = {
        'title' : 'about',
        'heading': 'about us',
    }
    return render(request, 'about.html')

def gallery(request):
    context = {
        'title' : 'gallery',
        'heading': 'galery sipena',
    }
    return render(request, 'gallery.html')