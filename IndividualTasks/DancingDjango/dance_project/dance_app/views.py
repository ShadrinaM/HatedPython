from django.shortcuts import redirect, render, get_object_or_404

from .forms import DancerForm, GroupForm, FestivalForm
from .models import Dancer, Festival, Group

def home(request):
    dancers = Dancer.objects.all()
    return render(request, 'home.html', {'dancers': dancers})

def dancer_detail(request, pk):
    dancer = get_object_or_404(Dancer, pk=pk)
    return render(request, 'dancer_detail.html', {'dancer': dancer})

def add_dancer(request):
    if request.method == "POST":
        form = DancerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DancerForm()
    return render(request, 'add_dancer.html', {'form': form})

def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GroupForm()
    return render(request, 'add_group.html', {'form': form})

def add_festival(request):
    if request.method == 'POST':
        form = FestivalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FestivalForm()
    return render(request, 'add_festival.html', {'form': form})



def home(request):
    dancers = Dancer.objects.all()
    groups = Group.objects.all()
    festivals = Festival.objects.all()
    
    context = {
        'dancers': dancers,
        'groups': groups,
        'festivals': festivals,
    }
    
    return render(request, 'home.html', context)

def dancer_detail(request, pk):
    dancer = get_object_or_404(Dancer, pk=pk)

    if request.method == 'POST':
        form = DancerForm(request.POST, instance=dancer)
        if form.is_valid():
            form.save()
            return redirect('dancer_detail', pk=dancer.pk)  # Перенаправление на ту же страницу после сохранения
    else:
        form = DancerForm(instance=dancer)

    return render(request, 'dancer_detail.html', {'dancer': dancer, 'form': form})