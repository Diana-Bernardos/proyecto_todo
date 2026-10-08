from django.db import models

# Create your models here.
from django.db import models

class Tareas(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('COMPLETADA', 'Completada'),
    ]

    nombre_tarea = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='')
    usuario = models.ForeignKey('Usuarios', on_delete=models.PROTECT)
    estado = models.ForeignKey('Estados', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre_tarea} - {self.estado}"
      
class Usuarios(models.Model):
  
    nombre_usuario = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"{self.nombre_usuario} {self.apellido}"    


class Estados(models.Model):
    nombre_estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_estado
