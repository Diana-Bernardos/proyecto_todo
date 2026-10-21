from django.db import models
from django.contrib.auth.models import User

class Tareas(models.Model):
    nombre_tarea = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas') #permite enlazar cada usuario con su respectiva tarea 
    estado = models.ForeignKey('Estados', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre_tarea}"
    
class Estados(models.Model):
    nombre_estado = models.CharField(max_length=49)

    def __str__(self):
        return self.nombre_estado
