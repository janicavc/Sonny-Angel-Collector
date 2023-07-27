from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sonny
from .forms import InspectForm

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
    inspect_form = InspectForm()
    return render(request, 'sonnyangels/detail.html', {
        'sonnyangel': sonnyangel, 'inspect_form': inspect_form
    })

class SonnyCreate(CreateView):
    model = Sonny
    fields = '__all__'

class SonnyUpdate(UpdateView):
    model = Sonny
    fields = ['series', 'description']

class SonnyDelete(DeleteView):
    model = Sonny
    success_url = '/sonnyangels'
