from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Sonny, Outfit
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
    id_list = sonnyangel.outfits.all().values_list('id')
    outfits_sonnyangel_doesnt_have = Outfit.objects.exclude(id__in=id_list)
    inspect_form = InspectForm()
    return render(request, 'sonnyangels/detail.html', {
        'sonnyangel': sonnyangel, 'inspect_form': inspect_form,
        'outfits': outfits_sonnyangel_doesnt_have
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

def add_inspect(request, sonnyangel_id):
    form = InspectForm(request.POST)
    if form.is_valid():
        new_inspect = form.save(commit=False)
        new_inspect.sonnyangel_id = sonnyangel_id
        new_inspect.save()
    return redirect('detail', sonnyangel_id=sonnyangel_id)

class OutfitList(ListView):
  model = Outfit

class OutfitDetail(DetailView):
  model = Outfit

class OutfitCreate(CreateView):
  model = Outfit
  fields = '__all__'

class OutfitUpdate(UpdateView):
  model = Outfit
  fields = ['type', 'color']

class OutfitDelete(DeleteView):
  model = Outfit
  success_url = '/outfits'

def assoc_outfit(request, sonnyangel_id, outfit_id):
  Sonny.objects.get(id=sonnyangel_id).outfits.add(outfit_id)
  return redirect('detail', sonnyangel_id=sonnyangel_id)

def unassoc_outfit(request, sonnyangel_id, outfit_id):
  Sonny.objects.get(id=sonnyangel_id).outfits.remove(outfit_id)
  return redirect('detail', sonnyangel_id=sonnyangel_id)