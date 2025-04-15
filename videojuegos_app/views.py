from django.shortcuts import render, redirect
from .forms import DesarrolladorForm, VideojuegoForm, PlataformaForm
from .models import Videojuego
from django.db.models import Q
from django.http import HttpResponse

def inicio(request):
    return render(request, 'vistas/inicio.html')

def agregar_desarrollador(request):
    if request.method == 'POST':
        form = DesarrolladorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_desarrollador')
    else:
        form = DesarrolladorForm()
    return render(request, 'vistas/agregar_desarrollador.html', {'form': form})

def agregar_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_videojuego')
    else:
        form = VideojuegoForm()
    return render(request, 'vistas/agregar_videojuego.html', {'form': form})

def agregar_plataforma(request):
    if request.method == 'POST':
        form = PlataformaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_plataforma')
    else:
        form = PlataformaForm()
    return render(request, 'vistas/agregar_plataforma.html', {'form': form})

def buscar_videojuego(request):
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Videojuego.objects.filter(
            Q(titulo__icontains=query)
        )
    return render(request, 'vistas/buscar_videojuego.html', {
        'resultados': resultados,
        'query': query
    })
