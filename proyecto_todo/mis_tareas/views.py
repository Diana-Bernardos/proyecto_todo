from django.shortcuts import render
from django.http import HttpRequest
from django.template import loader

def prueba(request):
    return render(request, 'mis_tareas/usuarios.html')


def crear_tarea(request):
    return render(request, 'mis_tareas/crear_tarea.html')
  
def editar_tarea(request):
    return render(request, 'mis_tareas/editar_tarea.html')

def eliminar_tarea(request):
    return render(request, 'mis_tareas/eliminar_tarea.html')