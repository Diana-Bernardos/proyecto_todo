from django import forms
from .models import Tareas, Usuarios, Estados

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields =['nombre_tarea', 'descripcion', 'estado']

clas

