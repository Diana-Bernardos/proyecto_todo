from django.urls import path
from . import views
urlpatterns = [

    path('prueba/', views.prueba),
    path('editar/', views.editar_tarea),
    path('añadir/', views.crear_tarea),
    path('usuarios/', views.usuario,name='usuario'),
    path('main/', views.main, name='main'),
    path('editar/<int:tareas_id>/', views.editar_tarea, name='editar'),
    path('inicio/', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('privado/',views.inicio_privado, name='privado'),
]

