from django.shortcuts import render

# Create your views here.
sonnyangels = [
    {'name': 'Shark' , 'series': 'Marine' , 'description': 'Classic marine animal!' },
    {'name': 'Chipmunk' , 'series': 'Animal Series 1' , 'description': 'Rare and cute!' }
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



