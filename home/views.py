from django.shortcuts import render, Http404, get_object_or_404
from django.db.models import Q
from .models import Games

def index(request): 
    dados = Games.objects.order_by('-id').filter(
        mostrar=True
    )
    return render(request,'home/index.html',{'dados':dados})

# Create your views here.
