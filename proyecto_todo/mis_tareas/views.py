from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.template import loader
from .forms import TareaForm
from .models import Tareas, Estados
import calendar
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def prueba(request):
    prueba1 = {
        'tarea': ['tarea1', 'tarea2']
        }
    return render(request, 'mis_tareas/main.html', prueba1)

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario_nuevo = form.save()
            login(request, usuario_nuevo)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'mis_tareas/registro.html', {'form': form})

def login_view(request):
    return render(request, 'mis_tareas/login.html')

@login_required
def main(request):
    ahora = datetime.now()
    anio = int(request.GET.get('anio', ahora.year))
    mes = int(request.GET.get('mes', ahora.month))
    if mes == 1:
        mes_anterior, anio_anterior = 12, anio -1
    else:
        mes_anterior, anio_anterior = mes -1, anio

    if mes == 12:
        mes_siguiente , anio_siguiente = mes +1, anio +1
    else:
        mes_siguiente, anio_siguiente = mes +1, anio

    cal = calendar.Calendar(firstweekday=0)
    calendar_matrix = cal.monthdayscalendar(anio, mes)

    tarea = Tareas.objects.filter(
            usuario = request.user,  
            fecha_vencimiento__year = anio,
            fecha_vencimiento__month = mes).select_related('estado').order_by('-fecha_creacion')  

    context = {
    'tarea': tarea,
    'calendar_matrix': calendar_matrix,
    'mes_actual': mes,
    'anio_actual': anio,
    'mes_anterior': mes_anterior,
    'anio_anterior': anio_anterior,
    'mes_siguiente': mes_siguiente,
    'anio_siguiente': anio_siguiente
    }
    return render(request, 'mis_tareas/main.html', context)

@login_required(login_url='login')
def inicio_privado(request):
    return render(request, 'mis_tareas/inicio_privado.html')

@login_required
def crear_tarea(request):
    fecha_inicial = request.GET.get('fecha', None)

    if request.method == 'POST':
        form = TareaForm(request.POST)

        if form.is_valid():
            tarea = form.save(commit=False)   
            tarea.usuario = request.user
            tarea.save()                      
            return redirect('inicio')
    else:
        initial_data ={}
        if fecha_inicial:
            initial_data['fecha_vencimiento'] = fecha_inicial
        form = TareaForm(initial=initial_data)
    return render(request, 'mis_tareas/añadir_tareas.html', {'form': form})

@login_required
def editar_tarea(request, tareas_id):
    tarea = get_object_or_404(Tareas, id= tareas_id)

    if request.method == "POST":
        if 'eliminar' in request.POST:
            tarea.delete()
            return redirect('inicio')
        
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        
    else:
        form = TareaForm(instance=tarea)

    return render(request, 'mis_tareas/editar_tareas.html', {'form':form})



