from django.shortcuts import render
from django.http import HttpRequest
from django.template import loader
from .forms import TareaForm

def prueba(request):
    return render(request, 'mis_tareas/usuarios.html')


def crear_tarea(request):
<<<<<<< HEAD
    return render(request, 'mis_tareas/añadir_tareas.html')
  
def editar_tarea(request):
    return render(request, 'mis_tareas/editar_tareas.html')
=======
    return render(request, 'mis_tareas/crear_tarea.html')

def editar_tarea(request):
    form = TareaForm
    return render(request, 'mis_tareas/editar_tareas.html', {'form':form})
>>>>>>> 77bbf2a0b566e92b1e84ba338e8ef6730e9fb7aa

def eliminar_tarea(request):
    return render(request, 'mis_tareas/eliminar_tareas.html')