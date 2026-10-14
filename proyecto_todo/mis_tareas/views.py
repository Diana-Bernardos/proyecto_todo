from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.template import loader
from .forms import TareaForm
from .models import Tareas, Estados, Usuarios
import calendar
from datetime import datetime

def prueba(request):
    prueba1 = {
        'tarea': ['tarea1', 'tarea2']
        }
    return render(request, 'mis_tareas/main.html', prueba1)

def main(request):
    ahora = datetime.now()
    anio = int(ahora.year)
    mes = int(ahora.month)

    # Genera la matriz del mes (empezando en domingo o lunes)
    cal_data = calendar.monthcalendar(anio, mes)
    nombre_mes = calendar.month_name[mes]

    tarea = Tareas.objects.all()  

    context = {
    'tarea': tarea,
    'calendar_matrix': cal_data,
    'mes_actual': nombre_mes,
    'anio_actual': anio,
    }
    return render(request, 'mis_tareas/main.html', context)


def crear_tarea(request):
    fecha_inicial = request.GET.get('fecha', None)

    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            estado_texto = request.POST.get('estado', '').strip().capitalize()
            objeto_estado, creado = Estados.objects.get_or_create(nombre_estado=estado_texto)
            tarea = form.save(commit=False)   
            tarea.estado = objeto_estado     
            tarea.save()                      
            return redirect('main')
    else:
        initial_data ={}
        if fecha_inicial:
            initial_data['fecha_vencimiento'] = fecha_inicial
        form = TareaForm(initial=initial_data)
    return render(request, 'mis_tareas/añadir_tareas.html', {'form': form})

def editar_tarea(request, tareas_id):
    tarea = get_object_or_404(Tareas, id= tareas_id)
    if request.method == "POST":
        if 'eliminar' in request.POST:
            tarea.delete()
            return redirect('main')
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'mis_tareas/editar_tareas.html', {'form':form})

def eliminar_tarea(request):
    return render(request, 'mis_tareas/eliminar_tareas.html')

def lista(request):
    return render(request, 'mis_Tareas/lista_tareas.html')