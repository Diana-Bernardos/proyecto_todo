from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.template import loader
from .forms import TareaForm, UsuarioForm
from .models import Tareas, Estados, Usuarios
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

def login_view(request):
    return render(request, 'mis_tareas/login.html')

@login_required
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

@login_required(login_url='login')
def inicio_privado(request):
    return render(request, 'mis_tareas/inicio_privado.html')


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
            return redirect('inicio')
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
            return redirect('inicio')
        
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            tarea_editada= form.save(commit=False)

            nombre_estado_ingresado = form.cleaned_data.get('estado')

            if nombre_estado_ingresado:

                estado_objeto, creado = Estados.objects.get_or_create(nombre_estado=nombre_estado_ingresado)
                tarea_editada.estado = estado_objeto
            else:
                tarea_editada.estado = None

            tarea_editada.save()
            return redirect('inicio')
    else:
        estado_inicial = tarea.estado.nombre_estado if tarea.estado else ''

        form = TareaForm(instance=tarea, initial={'estado':estado_inicial})

    return render(request, 'mis_tareas/editar_tareas.html', {'form':form})

def usuario(request):
    if request.method=='POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form=UsuarioForm()

    return render(request, 'mis_tareas/usuarios.html', {'form':form})

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