from django.urls import path
from . import views
urlpatterns = [
    path('prueba/', views.prueba),
    path('editar/', views.editar_tarea),
    path('añadir/', views.crear_tarea),
    path('lista/', views.lista),
    path('main/', views.main, name='main'),
    path('editar/<int:tareas_id>/', views.editar_tarea, name='editar')
]

