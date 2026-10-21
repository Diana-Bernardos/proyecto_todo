from django import forms
from .models import Tareas, Estados

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tareas
        fields =['nombre_tarea', 'descripcion', 'fecha_vencimiento', 'estado']
        widgets = {
            'fecha_vencimiento': forms.DateInput(
                format = '%Y-%m-%d',
                attrs = {'type': 'date'})
        }

