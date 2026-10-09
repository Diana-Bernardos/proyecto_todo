from django.urls import path
from . import views
urlpatterns = [
    path('prueba/', views.prueba),
    path('editar/', views.editar_tarea)
]
