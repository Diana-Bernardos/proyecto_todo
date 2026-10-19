from django.urls import path
from . import views
urlpatterns = [
    path('prueba/', views.prueba),
    path('editar/<int:tareas_id>/', views.editar_tarea, name='editar'),
    path('añadir/', views.crear_tarea, name='crear_tarea'),
    path('usuarios/', views.usuario, name='usuario'),
    path('main/', views.main, name='main'),
    path('inicio/', views.main, name='inicio'),
    path('privado/', views.inicio_privado, name='inicio_privado'),
]
