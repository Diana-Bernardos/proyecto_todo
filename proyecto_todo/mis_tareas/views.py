from django.shortcuts import render
from django.http import HttpRequest
from django.template import loader
from .forms import TareaForm

def prueba(request):
    return render(request, 'mis_tareas/usuarios.html')


def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)   
            tarea.usuario = request.user      
            tarea.save()                      
            return render(request, 'mis_tareas/añadir_tareas.html')
    else:
        form = TareaForm()
    return render(request, 'mis_tareas/añadir_tareas.html', {'form': form})
  
  
    
  
def editar_tarea(request):
    form = TareaForm
    return render(request, 'mis_tareas/editar_tareas.html', {'form':form})

def eliminar_tarea(request):
    return render(request, 'mis_tareas/eliminar_tareas.html')