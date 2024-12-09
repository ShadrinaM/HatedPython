from django.shortcuts import redirect, render, get_object_or_404

from .forms import DancerForm
from .models import Dancer

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

def home(request):
    # Получаем всех танцоров
    dancers = Dancer.objects.all()
    # Передаем танцоров в шаблон
    return render(request, 'home.html', {'dancers': dancers})

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