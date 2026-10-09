from django.shortcuts import render
from django.http import HttpRequest
from django.template import loader

def prueba(request):
    return render(request, 'mis_tareas/usuarios.html')
