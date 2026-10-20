from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="inicio_raiz"),
    path('prueba/', views.prueba),
    path('editar/', views.editar_tarea, name="editar"),
    path('añadir/', views.crear_tarea, name="crear_tarea"),
    path('usuarios/', views.usuario,name='usuario'),
    path('main/', views.main, name='inicio'),
    path('editar/<int:tareas_id>/', views.editar_tarea, name='editar_id'),
   
]
