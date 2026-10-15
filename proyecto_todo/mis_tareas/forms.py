from django import forms
from .models import Tareas, Usuarios, Estados

class TareaForm(forms.ModelForm):
    estado= forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Escribe el estado de tu tarea'}
        )
    )
    class Meta:
        model = Tareas
        fields =['nombre_tarea', 'descripcion', 'fecha_vencimiento']
        widgets = {
            'fecha_vencimiento': forms.DateInput(
                format = '%Y-%m-%d',
                attrs = {'type': 'date'})
        }

class UsuarioForm(forms.ModelForm):
    class Meta():
        model = Usuarios
        fields= ['nombre_usuario']
        

