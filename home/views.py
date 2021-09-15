import main
from django.shortcuts import render
from django.db.models import Q
from .models import Games

def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        games = Games.objects.filter(Q(title__icontains=search) | Q(releases__icontains=search) | Q(price__icontains=search) | Q(description__icontains=search) | Q(photos__icontains=search))
        return render(request, 'home/index.html', {'games':games})
    else:
        return render(request, 'home/index.html')

def index(request):
    return render(request, 'home/index.html')


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        releases = request.POST.get('releases')
        price = request.POST.get('price')
        description = request.POST.get('description')
        photos = request.POST.get('photos')
        game = Games(title=title,releases=releases,price=price,description=description,photos=photos)
        game.save()
        return render(request, 'home/index.html')
    else:
        return render(request, 'home/index.html')

def read(request):
    games = Games.objects.all()
    return render(request, 'home/index.html', {'games':games})


def update(request,id):
    game = Games.objects.get(id=id)
    if request.method == 'POST':
        game.title = request.POST.get('title')
        game.releases = request.POST.get('releases')
        game.price = request.POST.get('price')
        game.description = request.POST.get('description')
        game.photos = request.POST.get('photos')
        game.save()
        return render(request, 'home/index.html')
    else:
        return render(request, 'home/index.html', {'game':game})


def delete(request,id):
    game = Games.objects.get(id=id)
    game.delete()
    return render(request, 'home/index.html')
