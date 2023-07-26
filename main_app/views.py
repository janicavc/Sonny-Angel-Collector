from django.shortcuts import render
from .models import Sonny

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sonnyangels_index(request):
    sonnyangels = Sonny.objects.all()
    return render(request, 'sonnyangels/index.html', {
        'sonnyangels': sonnyangels
    })

def sonnyangels_detail(request, sonnyangel_id):
    sonnyangel = Sonny.objects.get(id=sonnyangel_id)
    return render(request, 'sonnyangels/detail.html', {
        'sonnyangel': sonnyangel
    })
